from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import FoodItem, Menu, Order, OrderItem

from email_service.views  import send_order_confirmation_email ,send_emails


@method_decorator(login_required, name='dispatch')
class OrderItemsView(View):
    def post(self, request):
        if 'confirm_order' in request.POST:
            return self.confirm_order(request)

        quantities = {key: value for key, value in request.POST.items() if key.startswith('quantities_')}
        ordered_menus = {}
        total_amount = 0

        for key, quantity in quantities.items():
            if not quantity.isdigit() or int(quantity) <= 0:
                continue

            _, menu_id, item_id = key.split('_')

            food_item = FoodItem.objects.get(id=item_id)
            menu = Menu.objects.get(id=menu_id)

            item_total = food_item.price * int(quantity)
            total_amount += float(item_total)  # Convert Decimal to float for JSON serialization

            if menu_id not in ordered_menus:
                ordered_menus[menu_id] = []
            ordered_menus[menu_id].append({
                'food_item_id': food_item.id,
                'quantity': int(quantity),
                'item_price': float(food_item.price)  # Convert Decimal to float for JSON serialization
            })

        if not ordered_menus:
            return render(request, 'orders/order_placement.html', {
                'error': 'No items selected. Please select items to order.'
            })

        # Store menu IDs and food item details in the session
        request.session['ordered_menus'] = ordered_menus
        request.session['total_amount'] = total_amount

        return render(request, 'orders/order_placement.html', {
            'ordered_menus': ordered_menus,
            'total_amount': total_amount,
            'user': request.user
        })

    def confirm_order(self, request):
        # Retrieve data from session
        ordered_menus = request.session.get('ordered_menus', {})
        total_amount = request.session.get('total_amount', 0.0)
        total_amount_per_menu = []
        display_total_amount_per_menu=[]
        # Reconstruct ordered menus with actual model objects
        reconstructed_menus = {}
        for menu_id, items in ordered_menus.items():
            total_amount = 0
            menu = Menu.objects.get(id=menu_id)
            reconstructed_menus[menu] = []

            for item in items:
                food_item = FoodItem.objects.get(id=item['food_item_id'])
                quantity = item['quantity']
                item_price = item['item_price']
                print("item_price", item_price)
                total_amount += item_price
                reconstructed_menus[menu].append((food_item, quantity, item_price))
            total_amount_per_menu.append(total_amount)
            display_total_amount_per_menu.append(total_amount * quantity)
        print("total_amount_per_menu", total_amount_per_menu)
        print("total_amodisplay_total_amount_per_menuunt_per_menu", display_total_amount_per_menu)
        total_amount = sum(total_amount_per_menu)
        if total_amount == 0.0:
            return redirect('WeeklyMenu')
        # Handle delivery options and delivery fees
        delivery_option = request.POST.get('delivery_option')
        delivery_fee = 0.0

        if delivery_option == 'home_delivery':
            if total_amount < 50.0:
                delivery_fee = 5.0  # Add delivery fee if the total amount is less than $50

        final_total = total_amount + delivery_fee

        # Create a new order
        order = Order.objects.create(
            user=request.user,
            total_amount=final_total
        )
        # Set session flag for order confirmation
        request.session['order_confirmed'] = True
        # Add ordered items to the order
        for menu, items in reconstructed_menus.items():
            for food_item, quantity, item_price in items:
                OrderItem.objects.create(
                    order=order,
                    menu=menu,
                    food_item=food_item,
                    quantity=quantity,
                    item_price=item_price
                )

        # Clear session data after order placement
        request.session.pop('ordered_menus', None)
        request.session.pop('total_amount', None)

        
        #send_order_confirmation_email(request)  # Send the email

        # send_order_confirmation_email(request,'farazahmed204@gmail.com' ,context={
        #     'ordered_menus': reconstructed_menus,
        #     'total_amount': total_amount,
        #     'delivery_option': delivery_option,
        #     'delivery_fee': delivery_fee,
        #     'final_total': final_total,
        #     'display_total_amount_per_menu':display_total_amount_per_menu
        # })
       # reconstructed_menus       
        # Render the order confirmation page
        return render(request, 'orders/order_confirmation.html', {
            'ordered_menus': reconstructed_menus,
            'total_amount': total_amount,
            'delivery_option': delivery_option,
            'delivery_fee': delivery_fee,
            'final_total': final_total,
            'display_total_amount_per_menu':display_total_amount_per_menu
        })
