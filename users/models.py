import jwt

from datetime import datetime, timedelta

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from UsersBudgeting.settings import SECRET_KEY


class UserManager(BaseUserManager):
    """
    Мэнэджер для работы с пользователями.
    """

    def create_user(self, username, email, password=None):
        """
        Создает и возвращает пользователя с эмэйлом, паролем и именем.
        """

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.activation_key_expired = timezone.now() + timedelta(days=1)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Создает и возвращет пользователя с привилегиями супер-пользователя.
        """

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    """
    Расширенная модель пользователя.
    """

    username = models.CharField(
        max_length=100,
        verbose_name="Имя пользователя",
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name="Показатель активности пользователя",
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    amount_exceeding = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма до превышения",
        help_text="Сумма которой не хватает до превышения бюджета,"
                  "после которой пользователь получит уведомление.",
        default=100
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        expiration_time = datetime.utcnow() + timedelta(hours=24)
        payload = {
            'user_id': self.id,
            'exp': expiration_time,
            'scope': self.is_staff
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return token

    @staticmethod
    def is_token_blacklisted(token):
        return BlacklistedToken.objects.filter(token=token).exists()


class BlacklistedToken(models.Model):
    token = models.CharField(
        max_length=255,
        unique=True
    )
    blacklisted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = "Черный список токенов"
        verbose_name_plural = "Черный список токенов"
