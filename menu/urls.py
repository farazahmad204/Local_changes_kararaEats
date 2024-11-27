from django.urls import path
from .views import DisplayMenuView, CreateMenuView, EditMenuView, DeleteMenuView,WeeklyMenuDisplay
from .import views
urlpatterns = [
    #path('dashboard/', MenuDashboardView.as_view(), name='menu_dashboard'),
    #path('', DisplayUserMenuView.as_view(), name='display_menu_user'),
    path('menu/', DisplayMenuView.as_view(), name='display_menu'),
    path('create/', CreateMenuView.as_view(), name='create_menu'),
    path('edit/<int:pk>/', EditMenuView.as_view(), name='edit_menu'),
    path('delete/<int:pk>/', DeleteMenuView.as_view(), name='delete_menu'),

    # Weekly Display
    path('Weeklymenu/', views.WeeklyMenuDisplay, name='WeeklyMenu'),


]
