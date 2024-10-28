from django.urls import path
from .views import OrderItemsView

urlpatterns = [
    # other paths
    path('order-items/', OrderItemsView.as_view(), name='order_items'),  # Add this line
    path('order-items/confirm/', OrderItemsView.as_view(), name='confirm_order'),
]