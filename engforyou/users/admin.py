from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# users/admin.py

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'age')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'age')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'age'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
