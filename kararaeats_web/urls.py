"""
URL configuration for kararaeats_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from kararaeats_web import settings
from kararaeats_web.views import  *  # Import your custom view

#handler404 = custom_page_not_found_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('special_home/', SpecialHomeView.as_view(), name='special_home'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
   # path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('order_status/', HomeView.as_view(), name='order_status'),
    path('', include('accounts.urls')),  # Include the accounts app URLs
    path('menu/', include('menu.urls')),
    path('', include('fooditems.urls')),  # Include the accounts app URLs
    path('orders/', include('order.urls')),

    path('email_service/',include('email_service.urls')),  # Include the Email app URLs

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)