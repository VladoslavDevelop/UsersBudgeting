from drf_yasg import openapi


def requests_create_transaction():
    """
    Документация для запроса при создании транзакции.
    """

    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['category_id', 'amount', 'type'],
        properties={
            'category_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID категории'),
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Сумма транзакции'),
            'type': openapi.Schema(type=openapi.TYPE_STRING, description='Тип транзакции'),
        },
        example={
            "category_id": 10,
            "amount": 300000,
            "type": "expense"
        }
    )


def response_create_transaction():
    """
    Документация для ответа при создании транзакции.
    """

    return {
        201: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "id": 10,
                    "uuid": "JBZ4yRnfLQTgt448",
                    "user_obj": {
                        "id": 5,
                        "email": "user@user2.com"
                    },
                    "category_obj": {
                        "id": 10,
                        "name": "Бензин"
                    },
                    "type": "expense",
                    "amount": 300000.0,
                    "description": "None",
                    "created_at": "2024-07-05 07:18:59.006183+00:00",
                    "is_active": True,
                    "attention_msg": False
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


def response_list_transaction():
    """
    Документация для ответа при получении списка транзакций.
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
                            "uuid": "JBZ4yRnfLQTgt448",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "type": "expense",
                            "amount": 300000.0,
                            "description": "None",
                            "created_at": "2024-07-05 07:18:59.006183+00:00",
                            "is_active": True,
                            "attention_msg": False
                        },
                        {
                            "id": 11,
                            "uuid": "1JfZ4yRnfadsdt448",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "type": "expense",
                            "amount": 3000.0,
                            "description": "None",
                            "created_at": "2024-07-05 07:18:59.006183+00:00",
                            "is_active": True,
                            "attention_msg": False
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


def response_get_transactions():
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
                            "uuid": "1JfZ4yRnfadsdt448",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "type": "expense",
                            "amount": 3000.0,
                            "description": "None",
                            "created_at": "2024-07-05 07:18:59.006183+00:00",
                            "is_active": True,
                            "attention_msg": False
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


def response_delete_transactions():
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
                            "uuid": "1JfZ4yRnfadsdt448",
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "type": "expense",
                            "amount": 3000.0,
                            "description": "None",
                            "created_at": "2024-07-05 07:18:59.006183+00:00",
                            "is_active": False,
                            "attention_msg": False
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
