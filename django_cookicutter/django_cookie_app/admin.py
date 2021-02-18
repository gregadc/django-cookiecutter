from django.contrib import admin

from django_cookie_app import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'date_joined', 'avatar']
    list_filter = ('email', 'username', 'date_joined')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'date',
        'price',
    ]
    list_filter = ('date',)
