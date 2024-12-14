
from decimal import Decimal

from menu.models import Menu, FoodItem
from order.models import  Order, OrderItem

class Cart:

    def __init__(self, request):
        self.session = request.session
        

        # Check if session already contains a cart
        cart = self.session.get('session_key')

        # If no cart exists for the user, initialize a new cart
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            print(f"Cart initialized with: {cart}")  # Debug print

        self.cart = cart
        self.item_count=0


    def add(self, menu_id, item_id, item_qty, item_price):
        # Print the values for debugging
        print(f"all items here from html: menu_id::{menu_id} item_id::{item_id}  item_qty::{item_qty} item_price::{item_price}")

        # Ensure the menu_id exists in the cart
        if str(menu_id) not in self.cart:
            self.cart[str(menu_id)] = {}  # Create a new dictionary for this menu if it doesn't exist

        # Check if the item already exists under the menu
        if str(item_id) in self.cart[str(menu_id)]:
            # If it exists, update the quantity (or modify other properties)
            current_qty = self.cart[str(menu_id)][str(item_id)]['qty']
            new_qty = current_qty + item_qty  # Optionally add to existing quantity
            self.cart[str(menu_id)][str(item_id)]['qty'] = new_qty
        else:
            # If the item doesn't exist, add it with its price and quantity
            self.cart[str(menu_id)][str(item_id)] = {'price': item_price, 'qty': item_qty}

        for item in self.cart.values():
            print(f"item in carts {item}")
        
        # Extract and print the desired structure
        for menu_id, items in self.cart.items():
            print(f"{menu_id}:")
            self.item_count = self.item_count + len(items)
            for item_id, details in items.items():
                price = details['price']
                qty = details['qty']
                print(f"  {item_id}: {{'price': {price}, 'qty': {qty}}}")


        # Mark the session as modified to save the cart
        self.session.modified = True
        print(f"Updated cart: {self.cart}")  # Debug print




    def delete(self, product):

        # product_id = str(product)

        # if product_id in self.cart:

        #     del self.cart[product_id]

        # self.session.modified = True
        pass



    def update(self, product, qty):

        # product_id = str(product)
        # product_quantity = qty

        # if product_id in self.cart:

        #     self.cart[product_id]['qty'] = product_quantity

        # self.session.modified = True
        pass


    def __len__(self):
        self.item_count=0
        # Extract and print the desired structure
        for menu_id, items in self.cart.items():
            print(f"{menu_id}:")
            self.item_count = self.item_count + len(items)
            print(f"self.item_counts are {self.item_count}")
        
        return self.item_count



    def __iter__(self):

        # all_product_ids = self.cart.keys()

        # products = Product.objects.filter(id__in=all_product_ids)

        # cart = self.cart.copy()

        # for product in products:

        #     cart[str(product.id)]['product'] = product

        # for item in cart.values():

        #     item['price'] = Decimal(item['price'])

        #     item['total'] = item['price'] * item['qty']

        #     yield item    
        pass

    
    def get_total(self):

        return 5
    
    def clear(self):
        """ Clears the cart by removing the 'session_key' from the session. """
        if 'session_key' in self.session:
            del self.session['session_key']  # Deletes the cart from the session
            self.session.modified = True  # Mark the session as modified to save changes
            print("Cart cleared.")




  


