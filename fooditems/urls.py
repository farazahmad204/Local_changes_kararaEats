from django.urls import path
from .views import EditFoodItemView, DeleteFoodItemView, DisplayFoodItemsView, CreateFoodItemView

urlpatterns = [
    path('food-items/', DisplayFoodItemsView.as_view(), name='food_items_management'),
    path('food-items/create', CreateFoodItemView.as_view(), name='create_food_item'),
    path('food-items/edit/<int:pk>/', EditFoodItemView.as_view(), name='edit_food_item'),
    path('food-items/delete/<int:pk>/', DeleteFoodItemView.as_view(), name='delete_food_item'),
]
