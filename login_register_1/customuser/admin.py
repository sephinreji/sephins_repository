from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile
from .forms import Registration


class CustomUserAdmin(UserAdmin):
    add_form = Registration
    model = UserProfile
    list_display = ('email','is_staff','is_active')


# Register your models here.
