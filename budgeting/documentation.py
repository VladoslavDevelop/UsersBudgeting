from drf_yasg import openapi


def requests_create_budgeting():
    """
    Документация для запроса при создании бюджета.
    """

    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['category_id', 'amount_budgeting'],
        properties={
            'category_id': openapi.Schema(type=openapi.TYPE_STRING, description='Id категории'),
            'amount_budgeting': openapi.Schema(type=openapi.TYPE_NUMBER, description='Сумма бюджета'),
        },
        example={
            "category_id": 4,
            "amount_budgeting": 5000000
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
                        "id": 3,
                        "user_obj": {
                            "id": 5,
                            "email": "user@user2.com"
                        },
                        "category_obj": {
                            "id": 10,
                            "name": "Бензин"
                        },
                        "amount_budgeting": 5000000.0,
                        "total_spent": 0.0,
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


def response_list_budgeting():
    """
    Документация для ответа при получении списка бюджетов.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": [
                        {
                            "id": 3,
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "amount_budgeting": 5000000.0,
                            "total_spent": 0.0,
                            "is_active": True
                        },
                        {
                            "id": 5,
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Покупки"
                            },
                            "amount_budgeting": 100000.0,
                            "total_spent": 0.0,
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


def response_get_budgeting():
    """
    Документация для ответа при получении бюджета.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": [
                        {
                            "id": 3,
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "amount_budgeting": 5000000.0,
                            "total_spent": 0.0,
                            "is_active": True
                        },

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


def response_delete_budgeting():
    """
    Документация для ответа при получении бюджета.
    """

    return {
        200: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": {
                    "status": "success",
                    "result": [
                        {
                            "id": 3,
                            "user_obj": {
                                "id": 5,
                                "email": "user@user2.com"
                            },
                            "category_obj": {
                                "id": 10,
                                "name": "Бензин"
                            },
                            "amount_budgeting": 5000000.0,
                            "total_spent": 0.0,
                            "is_active": False
                        },

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