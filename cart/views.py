from django.shortcuts import render

from .cart import Cart

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from menu.models import Menu
from fooditems.models import FoodItem


def cart_summary(request):

    cart = Cart(request)

    return render(request, 'cart/cart-summary.html', {'cart':cart})



def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        menu_id = int(request.POST.get('menu_id'))
        item_id=  int(request.POST.get('item_id'))
        qty = int(request.POST.get('qty'))

        
        print(f"Request is with menu_id {menu_id} and item_id{item_id} and qty{qty}")



        food_item = get_object_or_404(FoodItem, id=item_id)
        menu      = get_object_or_404(Menu, id=menu_id)

        print(f"extracted from database  is with menu_id {menu} and item_id{food_item} and qty{qty}")

        cart.add(menu=menu, food_item=food_item,item_qty=qty)



        cart_quantity = cart.__len__()


        #response = JsonResponse({'qty': cart_quantity})

        response = JsonResponse({'qty': cart_quantity})
        return response
        


def cart_delete(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})

        return response



def cart_update(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product=product_id, qty=product_quantity)


        cart_quantity = cart.__len__()

        cart_total = cart.get_total()


        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})

        return response

