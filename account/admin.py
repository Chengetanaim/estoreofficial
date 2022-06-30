from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Helps with better display on admin site

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'location', 'phone_number', 'profile_pic', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)