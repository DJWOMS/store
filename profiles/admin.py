from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профили пользователей"""
    list_display = ('user', 'first_name', 'last_name', 'phone')

