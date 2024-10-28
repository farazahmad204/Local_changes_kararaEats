from django.db import models
from fooditems.models import FoodItem


class Menu(models.Model):
    name = models.CharField(max_length=100)
    food_items = models.ManyToManyField(FoodItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
