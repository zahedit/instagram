from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin


class CustomeUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")

admin.site.register(User, CustomeUserAdmin)
