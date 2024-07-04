from django.contrib import admin

from .models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Админка для модели Categories.
    """

    list_display = ("id", "name", "is_active", "user",)
    search_fields = ("id", "name", "is_active", "user",)
    list_filter = ("id", "name", "is_active",)