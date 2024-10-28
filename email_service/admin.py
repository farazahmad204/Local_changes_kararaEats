from django.contrib import admin

# Register your models here.

from .models import Mail

#admin.site.register(Mail)

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ['name','email','slug','mobile']
    prepopulated_fields = {"slug":("name",)}

