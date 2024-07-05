from drf_yasg import openapi


def response_report_transaction():
    """
    Документация для ответа при получении отчетов по транзакциям.
    """

    return {
        201: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": [
                    {
                        "total_transactions": 2,
                        "income_percentage": 0.0,
                        "expense_percentage": 100.0,
                        "total_income_amount": 0,
                        "total_expense_amount": 600000.0,
                        "total_amount": 600000.0
                    },
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
                        "is_active": True
                    },
                    {
                        "id": 10,
                        "uuid": ";aoishg9843y9t",
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
                        "is_active": True
                    },
                ]
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


def response_report_analytic_categories():
    """
    Документация для ответа при получении аналитики
    """

    return {
        201: openapi.Response(
            description="Успешный запрос",
            examples={
                "application/json": [
                    {
                        "total_transactions": 2,
                        "income_percentage": 0.0,
                        "expense_percentage": 100.0,
                        "total_income_amount": 0,
                        "total_expense_amount": 600000.0,
                        "total_amount": 600000.0
                    },
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
                        "is_active": True
                    },
                    {
                        "id": 10,
                        "uuid": ";aoishg9843y9t",
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
                        "is_active": True
                    },
                ]
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