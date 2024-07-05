from drf_yasg import openapi


def request_registration():
    """
    Документация для запроса при регистрации.
    """

    return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password', 'password_confirm'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль пользователя'),
                'password_confirm': openapi.Schema(type=openapi.TYPE_STRING, description='Подтверждение пароля'),
            },
            example={
                "email": "user@user1.com",
                "password": "Example1",
                "password_confirm": "Example1"
            }
        )


def response_registration():
    """
    Документация для ответа при регистрации.
    """

    return {
            201: openapi.Response(
                description="Пользователь успешно создан",
                examples={
                    "application/json": {
                        "status": "success",
                        "result": {
                            "email": "user@user2.com",
                            "token": "eyJ0eXAiWxzZX0.4bbpQrbRLKsdGvSjzfs9VfUYPGcIhtzj0NlKwl9uf-k",
                            "is_active": True,
                            "is_active_staff": None
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Ошибка при создании пользователя",
                examples={
                    "application/json": {
                        "status": "error",
                        "result": "msg error"
                    }
                }
            )
        }


def request_login():
    """
    Документация для запроса при авторизации.
    """

    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email', 'password'],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль пользователя'),
        },
        example={
            "email": "admin@admin.com",
            "password": "Barselona1"
        }
    )


def response_login():
    """
    Документация для ответа при авторизации.
    """

    return {
        200: openapi.Response(
            description="Успешная авторизация",
            examples={
                "application/json": {
                    "status": "success",
                    "result": {
                        "email": "user@user2.com",
                        "token": "eyJ0eXAiWxzZX0.4bbpQrbRLKsdGvSjzfs9VfUYPGcIhtzj0NlKwl9uf-k",
                    }
                }
            }
        ),
        400: openapi.Response(
            description="Ошибка при регистрации",
            examples={
                "application/json": {
                    "status": "error",
                    "result": "msg error"
                }
            }
        )
    }


def response_logout():
    """
    Документация для запроса при выходе.
    """

    return {
        200: openapi.Response(
            description="Успешный выход",
            examples={
                "application/json": {
                    "status": "success",
                    "result": "Выход успешно осуществлен"
                }
            }
        ),
        400: openapi.Response(
            description="Ошибка при регистрации",
            examples={
                "application/json": {
                    "status": "error",
                    "result": "msg error"
                }
            }
        )
    }


def response_profile():
    """
    Документация для запроса при профиле.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": {
                        "id": 5,
                        "username": "user@user2.com",
                        "email": "user@user2.com",
                        "amount_exceeding": 100.0
                    }
                }
            }
        ),
        400: openapi.Response(
            description="Ошибка при регистрации",
            examples={
                "application/json": {
                    "status": "error",
                    "result": "msg error"
                }
            }
        )
    }


def requests_update_profile():
    """
    Документация для запроса при обновлении профиля.
    """

    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'email', 'amount_exceeding'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username пользователя'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
            'amount_exceeding': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='Если у пользователя есть бюджет на любую категорию, и разница между суммой транзакций в указанной категории и бюджетом на эту категорию будет меньше или равно этому полю, пользователь получит уведомление'
            ),
        },
        example={
            "username": "user@user2.com",
            "email": "user@user2.com",
            "amount_exceeding": 150.0
        }
    )


def response_update_profile():
    """
    Документация для ответа при обновлении профиля.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": {
                        "id": 5,
                        "username": "user@user2.com",
                        "email": "user@user2.com",
                        "amount_exceeding": 150.0
                    }
                }
            }
        ),
        400: openapi.Response(
            description="Ошибка при регистрации",
            examples={
                "application/json": {
                    "status": "error",
                    "result": "msg error"
                }
            }
        )
    }


def response_token_refresh():
    """
    Документация для ответа при обновлении токена.
    """

    return {
        200: openapi.Response(
            description="Успешная авторизация",
            examples={
                "application/json": {
                    "status": "success",
                    "result": {
                        "email": "user@user2.com",
                        "token": "eyJ0epmYWxzZX0.wvy3blLhhjKieiuq6MsE5NyI9GKxI5BJEwKUKm7UI60",
                        "is_active": True,
                        "is_active_staff": None
                    }
                }
            }
        ),
        400: openapi.Response(
            description="Ошибка при регистрации",
            examples={
                "application/json": {
                    "status": "error",
                    "result": "msg error"
                }
            }
        )
    }
