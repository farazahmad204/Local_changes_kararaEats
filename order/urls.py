from django.urls import path
from .views import OrderItemsView
from . import views

urlpatterns = [
    # other paths
    path('order-items/', OrderItemsView.as_view(), name='order_items'),  # Add this line
    path('order-items/confirm/', OrderItemsView.as_view(), name='confirm_order'),
    path('order-items/checkout_view/', views.checkout_view, name='checkout_view'),
]