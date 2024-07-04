from django.contrib import admin

from .models import BudgetingCategories

@admin.register(BudgetingCategories)
class BudgetingCategoriesAdmin(admin.ModelAdmin):
    """
    Админка для модели BudgetingCategories.
    """

    list_display = ("id", "user", "category", "amount_budgeting",)
    search_fields = ("id", "user", "category", "amount_budgeting",)
    list_filter = ("id", "user", "category",)
