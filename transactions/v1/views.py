import traceback

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from transactions.system.controller.TransactionController import TransactionController
from users.utils import JWTAuthentication
from transactions.documentation import *


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class TransactionView(APIView, TransactionController):
    """
    Получение списка транзакций.
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
        operation_summary='Создание транзакции',
        operation_description="Создание транзакции дохода/расхода",
        tags=['transactions'],
        security=["JWT"],
        request_body=requests_create_transaction(),
        responses=response_create_transaction()
    )
    def post(self, request):
        """
        Создание записи о транзакции.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response, status=status.HTTP_400_BAD_REQUEST)
        try:
            self.create_obj()
            if self.error_data:
                return Response(self.error_response, status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при создании транзакции - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Получение списка транзакций',
        operation_description="Получение списка транзакций пользователя",
        tags=['transactions'],
        security=["JWT"],
        responses=response_list_transaction(),
    )
    def get(self, request):
        """
        Получение списка транзакций.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_data, status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_all_transactions()
            if self.error_data:
                return Response(self.error_data, status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при получении транзакции - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class TransactionDetailView(APIView, TransactionController):
    """
    Получение конкретной транзакции.
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
        operation_summary='Получение конкретной транзакции',
        operation_description="Получение конкретной транзакции пользователя",
        tags=['transactions'],
        security=["JWT"],
        responses=response_get_transactions(),
    )
    def get(self, request, pk):
        """
        Получение конкретной транзакции.
        :param request:
        :param pk:
        :return:
        """

        self.request = request
        self.pk = pk
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при получении транзакции - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Обновление транзакции',
        operation_description="Обновление конкретной транзакции пользователя",
        tags=['transactions'],
        security=["JWT"],
        request_body=requests_create_transaction(),
        responses=response_get_transactions(),
    )
    def put(self, request, pk):
        """
        Обновление конкретной транзакции.
        :param request:
        :param pk:
        :return:
        """

        self.request = request
        self.pk = pk
        self.post_data = request.data
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.update_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при обновлении транзакции - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Удаление транзакции',
        operation_description="Удаление конкретной транзакции пользователя",
        tags=['transactions'],
        security=["JWT"],
        responses=response_delete_transactions(),
    )
    def delete(self, request, pk):
        """
        Удаление конкретной транзакции.
        :param request:
        :param pk:
        :return:
        """

        self.request = request
        self.pk = pk
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.delete_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при удалении транзакции - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
