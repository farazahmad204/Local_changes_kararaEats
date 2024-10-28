from accounts.models import CustomUser
from django.db import models
from menu.models import Menu, FoodItem


class Order(models.Model):
    DELIVERY_OPTIONS = (
        ('self_pickup', 'Self-Pickup'),
        ('home_delivery', 'Home Delivery'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_option = models.CharField(max_length=15, choices=DELIVERY_OPTIONS)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.food_item.name} (x{self.quantity})"
