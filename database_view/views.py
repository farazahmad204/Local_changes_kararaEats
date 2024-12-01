from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from kararaeats_web.views import is_manager
from fooditems.models import FoodItem
from menu.models import Menu
from order.models import Order, OrderItem
from accounts.models import  CustomUser
from .serializers import FoodItemSerializer, MenuSerializer, OrderSerializer, OrderItemSerializer, CustomUserSerializer
from django.db.models import Q

# View for FoodItems Table
def food_items(request):
    filter_name = request.GET.get('name', '')
    filter_min_price = request.GET.get('price_min', '')
    filter_max_price = request.GET.get('price_max', '')

    food_items = FoodItem.objects.all()

    if filter_name:
        food_items = food_items.filter(name__icontains=filter_name)
    if filter_min_price:
        food_items = food_items.filter(price__gte=filter_min_price)
    if filter_max_price:
        food_items = food_items.filter(price__lte=filter_max_price)

    return render(request, 'database_view/food_items.html', {'food_items': food_items})

# View for Menu Table
def menu_items(request):
    menus = Menu.objects.all()
    return render(request, 'database_view/menu_items.html', {'menus': menus})

@login_required(login_url=reverse_lazy('login'))
@user_passes_test(is_manager,login_url=reverse_lazy('login'))
def orders_view(request):
    orders = Order.objects.all()

    # Get filter parameters from the request
    search_query = request.GET.get('search', '')
    delivery_option = request.GET.get('delivery_option', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    min_amount = request.GET.get('min_amount', '')
    max_amount = request.GET.get('max_amount', '')
    payment_status = request.GET.get('payment_status', '')  # New filter for payment status

    # Apply filters
    if search_query:
        orders = orders.filter(user__username__icontains=search_query)
    if delivery_option:
        orders = orders.filter(delivery_option=delivery_option)
    if start_date and end_date:
        orders = orders.filter(created_at__date__range=[start_date, end_date])
    elif start_date:
        orders = orders.filter(created_at__date__gte=start_date)
    elif end_date:
        orders = orders.filter(created_at__date__lte=end_date)
    if min_amount:
        orders = orders.filter(total_amount__gte=min_amount)
    if max_amount:
        orders = orders.filter(total_amount__lte=max_amount)
    if payment_status:  # Apply filter for payment status
        orders = orders.filter(payment_status=payment_status)

    # Pagination
    paginator = Paginator(orders, 10)  # Show 10 orders per page
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    return render(request, 'database_view/orders.html', {'orders': orders})
# View for Custom Users Table
def users(request):
    users = CustomUser.objects.all()
    return render(request, 'database_view/users.html', {'users': users})

# Filtered Orders Table
def filtered_orders(request):
    filter_date = request.GET.get('created_at', '')
    orders = Order.objects.all()

    if filter_date:
        orders = orders.filter(created_at__date=filter_date)

    return render(request, 'database_view/filtered_orders.html', {'orders': orders})
