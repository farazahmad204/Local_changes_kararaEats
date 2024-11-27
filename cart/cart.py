
from decimal import Decimal

from fooditems.models import FoodItem

from menu.models import Menu

class Cart():

    def __init__(self, request):

        self.session = request.session

        # Returning user - obtain his/her existing session

        cart = self.session.get('session_key')


        # New user - generate a new session

        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}

        print("cart is ", cart)

        self.cart = cart


    def add(self, menu=None, food_item=None, item_qty=None):
        menu_id = str(menu.id)  # Convert the menu ID to string
        item_id = str(food_item.id)  # Convert the food item ID to string
        price = food_item.price  # Get the price of the food item

        # Check if the menu already exists in the cart
        if menu_id not in self.cart:
            self.cart[menu_id] = {}  # Create a new dictionary for this menu ID

        # Check if the food item already exists in the cart for this menu
        if item_id in self.cart[menu_id]:
        # If the item already exists, update the quantity
            self.cart[menu_id][item_id]['qty'] = item_qty
        else:
            # Otherwise, add the item with its price and quantity
            self.cart[menu_id][item_id] = {'price': str(price), 'qty': item_qty}

        self.session.modified = True  # Mark the session as modified



    # def delete(self, product):

    #     product_id = str(product)

    #     if product_id in self.cart:

    #         del self.cart[product_id]

    #     self.session.modified = True



    # def update(self, product, qty):

    #     product_id = str(product)
    #     product_quantity = qty

    #     if product_id in self.cart:

    #         self.cart[product_id]['qty'] = product_quantity

    #     self.session.modified = True


    def __len__(self):

        print("self.cart.values() are ",self.cart.values())

        cart_items=self.cart.__len__()

        print("self.cart.values() lenght are  ",self.cart.__len__())

        return cart_items

        #return sum(int (item['qty']) for item in self.cart.values())



    def __iter__(self):
        """
        Iterate through the cart and update the data with readable menu names, item names,
        and the total price based on the quantity.
        """
        sub_total=0
        for menu_name, items in self.cart.items():  # Iterate through each menu
            print(f"Menu Name: {menu_name}")
            # Retrieve the menu object from the database using the menu_id
            menu_name = Menu.objects.get(id=menu_name)  # Assume you have a Menu model
            print("menu_name is ", menu_name)
        
        # Collect all the items for this menu
            menu_items = []

            for item_name, item_data in items.items():  # Iterate through items of the menu
                
                # Retrieve the food item object from the database using the item_id
                food_item = FoodItem.objects.get(id=item_name)  # Assume you have a FoodItem model
                item_name = food_item.name  # Get the food item name
                item_img  = food_item.picture
                item_price = float(item_data['price'])  # Get the item price as a float
                item_qty = int(item_data['qty'])  # Get the item quantity as an integer
                print(f"Item Name: {item_name}, Quantity: {item_qty}, Price: {item_price}, Image ::{item_img}")

            # Calculate the total price based on the quantity
                total_price = item_price * item_qty
                sub_total=sub_total + total_price

            # Add the item details to the menu's list of items
                menu_items.append({
                'item_name': item_name,
                'item_qty': item_qty,
                'item_price': item_price,
                'total_price': total_price,
                'item_img':item_img,
                'sub_total': sub_total
                })
           
            # Yield the menu details, including the name and list of items
            yield {'menu_name': menu_name, 'items': menu_items}

        


    
    def get_total(self):
        
        return (100)




  


