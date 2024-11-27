from django.contrib import admin
from .models import CustomUser

# Register your models here.
# Register CustomUser with the custom UserAdmin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'whatsapp_num', 'address', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'whatsapp_num')  # Enable searching by username, email, and whatsapp number
    list_filter = ('is_staff', 'is_active')  # Add filters for staff and active status

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
