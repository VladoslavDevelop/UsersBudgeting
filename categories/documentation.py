from drf_yasg import openapi


def requests_create_category():
    """
    Документация для запроса при создании бюджета.
    """

    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Название категории'),
        },
        example={
            "name": "Бензин"
        }
    )


def response_create_budgeting():
    """
    Документация для ответа при создании бюджета.
    """

    return {
        201: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": {
                        "id": 10,
                        "name": "Бензин",
                        "user_obj": {
                            "id": 5,
                            "email": "user@user2.com"
                        },
                        "is_active": True
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


def response_list_category():
    """
    Документация для ответа при получении списка категорий.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": [
                        {
                            "id": 10,
                            "name": "Бензин",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "is_active": True
                        },
                        {
                            "id": 11,
                            "name": "Покупки",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "is_active": True
                        }
                    ]
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


def response_get_category():
    """
    Документация для ответа при получении категории.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": [
                        {
                            "id": 11,
                            "name": "Покупки",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "is_active": True
                        }
                    ]
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


def response_delete_category():
    """
    Документация для ответа при получении категории.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": [
                        {
                            "id": 11,
                            "name": "Покупки",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "is_active": False
                        }
                    ]
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