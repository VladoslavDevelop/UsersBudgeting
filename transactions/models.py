from django.db import models

from users.models import User
from categories.models import Categories


class Transactions(models.Model):
    """Модель для работы с операциями доходов и расходов."""

    TRANSACTION_TYPE = (
        ('income', 'Доход'),
        ('expense', 'Расход')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='Пользователь'
    )
    uuid = models.CharField(
        max_length=255,
        verbose_name='UUID транзакции'
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    type = models.CharField(
        max_length=255,
        choices=TRANSACTION_TYPE,
        verbose_name='Тип транзакции'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма транзакции в рублях'
    )
    description = models.TextField(
        verbose_name='Описание транзакции',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания транзакции'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активность транзакции'
    )

    def __str__(self):
        return self.uuid

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
