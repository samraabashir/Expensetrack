from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Expense


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        ("ExpenseTrack Information", {"fields": ("role",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("ExpenseTrack Information", {"fields": ("role",)}),
    )

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "seller", "amount", "category", "date")
    list_filter = ("category", "date")