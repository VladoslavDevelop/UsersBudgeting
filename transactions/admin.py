from django.contrib import admin

from .models import Transactions


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    """
    Админка для модели Transactions.
    """

    list_display = ("id", "user", "uuid", "category", "type", "amount", "description", "created_at",)
    search_fields = ("id", "user", "uuid", "category", "type", "amount", "description", "created_at",)
    list_filter = ("user", "category", "type",)