import traceback

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from budgeting.system.controller.BudgetingController import BudgetingController
from users.utils import JWTAuthentication
from budgeting.documentation import *


@authentication_classes([JWTAuthentication])
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

    @swagger_auto_schema(
        operation_summary='Создание бюджета',
        operation_description="Создание бюджета пользователя",
        tags=['budgeting'],
        security=["JWT"],
        request_body=requests_create_budgeting(),
        responses=response_create_budgeting()
    )
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

    @swagger_auto_schema(
        operation_summary='Получение бюджетов',
        operation_description="Получение списка бюджетов пользователя",
        tags=['budgeting'],
        security=["JWT"],
        responses=response_list_budgeting(),
    )
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


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class BudgetingDetailView(APIView, BudgetingController):
    """
    Класс для работы с конкретным бюджетом.
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

    @swagger_auto_schema(
        operation_summary='Получение конкретного бюджета',
        operation_description="Получение конкретного бюджета пользователя",
        tags=['budgeting'],
        security=["JWT"],
        responses=response_get_budgeting(),
    )
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

    @swagger_auto_schema(
        operation_summary='Изменение конкретного бюджета',
        operation_description="Изменение конкретного бюджета пользователя",
        tags=['budgeting'],
        security=["JWT"],
        request_body=requests_create_budgeting(),
        responses=response_get_budgeting(),
    )
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

    @swagger_auto_schema(
        operation_summary='Удаление конкретного бюджета',
        operation_description="Удаление конкретного бюджета пользователя",
        tags=['budgeting'],
        security=["JWT"],
        responses=response_delete_budgeting(),
    )
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
