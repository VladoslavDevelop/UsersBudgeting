from django.db import models

from categories.models import Categories


class BudgetingCategories(models.Model):
    """
    Модель для создания определенных бюджетов в категориях.
    """

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    amount_budgeting = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма бюджета в рублях'
    )
    total_spent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма покупок в данной категории в рублях',
        default=0
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активность'
    )

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = 'Бюджет'
        verbose_name_plural = 'Бюджеты'
