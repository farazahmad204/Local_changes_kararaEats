from django.urls import path
from . import views

urlpatterns = [
    #path('food-items/', views.food_items, name='food_items'),
    #path('menus/', views.menu_items, name='menu_items'),
    path('orders/', views.orders_view, name='orders'),
    #path('users/', views.users, name='users'),
    #path('filtered-orders/', views.filtered_orders, name='filtered_orders'),
]
