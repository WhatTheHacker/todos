from django.contrib import admin
from .models import UserManager, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomerAdmin(UserAdmin):
    list_display = ('role', 'email', 'first_name', 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomerAdmin)
