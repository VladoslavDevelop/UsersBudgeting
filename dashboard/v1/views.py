import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from dashboard.system.controller.AdminCategoryController import AdminCategoriesController
from dashboard.system.controller.AdminTransactionController import AdminTransactionController
from dashboard.system.controller.AdminBudgetingController import AdminBudgetingController
from dashboard.system.controller.AdminUserController import AdminUserController
from dashboard.system.controller.AdminReportAnalyticController import AdminReportAnalyticController


@permission_classes([IsAdminUser])
class CategoryAllView(APIView, AdminCategoriesController):
    """
    Класс для получения всех категорий.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        """
        Получение всех категорий.
        :param request:
        :return:
        """
        _default_message = {
            'errors': {
                'field_not_provided': {
                    'en': 'Field {field_name} not provided',
                    'ru': 'Поле {field_name} не предоставлено'
                }
            }
        }

        self.post_data = request.data
        self.request = request
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_all_categories()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create category: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении категорий'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class CategoryDetailView(APIView, AdminCategoriesController):
    """
    Класс для работы с конкретной категорией.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def get(self, request, pk):
        """
        Получение всех категорий.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.pk = pk
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get categories: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении категорий'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class TransactionAllView(APIView, AdminTransactionController):
    """
    Класс для получения всех транзакций.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        """
        Получение всех транзакций.
        :param request:
        :return:
        """
        _default_message = {
            'errors': {
                'field_not_provided': {
                    'en': 'Field {field_name} not provided',
                    'ru': 'Поле {field_name} не предоставлено'
                }
            }
        }

        self.post_data = request.data
        self.request = request
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_all_transactions()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create transaction: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении транзакций'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class TransactionDetailView(APIView, AdminTransactionController):
    """
    Класс для работы с конкретной транзакцией.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def get(self, request, pk):
        """
        Получение всех транзакций.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.pk = pk
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get transaction: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении транзакций'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class BudgetAllView(APIView, AdminBudgetingController):
    """
    Класс для получения всех транзакций.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        """
        Получение всех транзакций.
        :param request:
        :return:
        """

        self.post_data = request.data
        self.request = request
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_budgeting_all()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create transaction: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении транзакций'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class BudgetDetailView(APIView, AdminBudgetingController):
    """
    Класс для работы с конкретной транзакцией.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def get(self, request, pk):
        """
        Получение всех транзакций.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.pk = pk
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_budgeting()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get transaction: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении транзакций'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class UserAllView(APIView, AdminUserController):
    """
    Класс для получения всех пользователей.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        """
        Получение всех пользователей.
        :param request:
        :return:
        """

        self.post_data = request.data
        self.request = request
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_all_users()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create user: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении пользователей'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class UserDetailView(APIView, AdminUserController):
    """
    Класс для работы с конкретным пользователем.
    """
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def get(self, request, pk):
        """
        Получение всех пользователей.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.pk = pk
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get users: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении пользователей'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class ReportsAllView(APIView, AdminReportAnalyticController):
    """
    Класс для получения всех отчетов.
    """
    _required_parameters = ['user_id']
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        """
        Получение отчета за конкретного пользователя.
        :param request:
        :return:
        """

        self.post_data = request.data
        self.request = request
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_reports()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create report: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении отчетов'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class AnalyticsAllView(APIView, AdminReportAnalyticController):
    """
    Класс для получения аналитики за конкретного пользователя.
    """
    _required_parameters = ['user_id']
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        """
        Получение всех аналитик.
        :param request:
        :return:
        """

        self.post_data = request.data
        self.request = request
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_analytic_category()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create analytic: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении аналитик'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
