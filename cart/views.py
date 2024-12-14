from django.shortcuts import render

from .cart import Cart

from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def cart_summary(request):

    cart = Cart(request)

    return render(request, 'cart/cart-summary.html', {'cart':cart})



def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        menu_id = int(request.POST.get('menu_id'))
        item_id = int(request.POST.get('item_id'))
        item_qty = int(request.POST.get('item_qty'))
        item_price = float(request.POST.get('item_price'))

        #product = get_object_or_404(Product, id=product_id)

        cart.add(menu_id, item_id, item_qty, item_price)


        cart_quantity = cart.__len__()
        print(f"cart quantity:: {cart_quantity}")


        response = JsonResponse({'qty': cart_quantity})

        return response
        


def cart_delete(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        # product_id = int(request.POST.get('product_id'))

        # cart.delete(product=product_id)


        # cart_quantity = cart.__len__()

        # cart_total = cart.get_total()


        response = JsonResponse({'qty':5, 'total':50})

        return response



def cart_update(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        # product_id = int(request.POST.get('product_id'))
        # product_quantity = int(request.POST.get('product_quantity'))

        # cart.update(product=product_id, qty=product_quantity)


        # cart_quantity = cart.__len__()

        # cart_total = cart.get_total()


        response = JsonResponse({'qty':5, 'total':500})

        return response

