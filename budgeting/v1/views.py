import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from budgeting.system.controller.BudgetingController import BudgetingController


@permission_classes([IsAuthenticated])
class BudgetingView(APIView, BudgetingController):
    """
    Класс для работы с бюджетом.
    """

    _required_parameters = []
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
        Создание бюджета.
        :param request:
        :return:
        """

        self.post_data = request.data
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.create_budgeting()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при создании бюджета'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Получение бюджета.
        :param request:
        :return:
        """
        self.post_data = request.data
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_budgeting_all()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при получении бюджета'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class BudgetingDetailView(APIView, BudgetingController):
    """
    Класс для работы с конкретным бюджетом.
    """

    def get(self, request, pk):
        """
        Получение бюджета по id.
        :param request:
        :param pk:
        :return:
        """
        self.pk = pk
        self.request = request
        self.validate_parameters(request)
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
            self.error_data = {
                'error': 'Ошибка при получении бюджета'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Обновление бюджета по id.
        :param request:
        :param pk:
        :return:
        """

        self.pk = pk
        self.request = request
        self.post_data = request.data
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.update_budgeting()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при обновлении бюджета'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Удаление бюджета по id.
        :param request:
        :param pk:
        :return:
        """

        self.pk = pk
        self.request = request
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.delete_budgeting()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при удалении бюджета'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)