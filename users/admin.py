from django.contrib import admin

from users.models import User, BlacklistedToken


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка для модели User.
    """

    list_display = ("id", "username", "email", "is_active", "is_staff",)
    search_fields = ("id", "username", "email", "is_active", "is_staff",)
    list_filter = ("username", "email",)


@admin.register(BlacklistedToken)
class BlacklistedTokenAdmin(admin.ModelAdmin):
    """
    Админка для модели BlacklistedToken.
    """

    list_display = ("id", "token",)
    search_fields = ("id", "token",)
