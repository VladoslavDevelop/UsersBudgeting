from Core.Serializer.BaseSerializer import BaseSerializer


class UserSerializer(BaseSerializer):
    """
    Сериализация пользователя.
    """

    fields = [
        'email',
        'token',
        'is_active',
        'is_active_staff',

    ]

    def __init__(self, entity):
        super().__init__(entity)


class UserAuthSerializer(BaseSerializer):
    """
    Сериализация при авторизации пользователя.
    """

    fields = [
        'email',
        'token'
    ]

    def __init__(self, entity):
        super().__init__(entity)


class UserShortSerializer(BaseSerializer):
    """
    Сериализация пользователя.
    """

    fields = [
        'id',
        'email',
    ]


class UserProfileSerializer(BaseSerializer):
    """
    Сериализация профиля пользователя.
    """

    fields = [
        'id',
        'username',
        'email',
        'amount_exceeding',
    ]
