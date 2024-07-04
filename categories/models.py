from django.db import models

from users.models import User


class Categories(models.Model):
    """
    Модель для работы с категориями транзакций.
    """

    name = models.CharField(
        max_length=255,
        verbose_name='Название категории'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активность категории'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='Пользователь'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

