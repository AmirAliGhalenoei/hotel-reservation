from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "phone", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["phone", "username"]
    ordering = ['username']
    filter_horizontal = ()

    fieldsets = (
        ("Information User",{"fields":("phone", "username", "email", "password")}),
        ("User Permissions",{"fields":("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        ("Register User",{"fields":("phone", "username", "email", "password1", "password2")}),
    )
admin.site.register(User,UserAdmin)
    
