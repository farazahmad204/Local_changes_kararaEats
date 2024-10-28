# fooditems/models.py

from django.db import models
from django.apps import apps


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='food_items/', blank=True, null=True)

    def get_menu(self):
        Menu = apps.get_model('menu', 'Menu')
        return Menu.objects.filter(food_items=self)

    def __str__(self):
        return self.name
