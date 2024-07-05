import traceback

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from categories.system.controller.CategoriesController import CategoriesController
from users.utils import JWTAuthentication
from categories.documentation import *


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CategoriesView(APIView, CategoriesController):
    """
    Api класс для работы с категориями.
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
        operation_summary='Создание категории',
        operation_description="Создание категории пользователя",
        tags=['categories'],
        security=["JWT"],
        request_body=requests_create_category(),
        responses=response_create_budgeting()
    )
    def post(self, request):
        """
        Метод для создания категории.
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
            self.create_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create category: {_error}")
            self.error_data = {
                'error': 'Ошибка при создании категории'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Получение категорий',
        operation_description="Получение списка категорий пользователя",
        tags=['categories'],
        security=["JWT"],
        responses=response_list_category(),
    )
    def get(self, request):
        """
        Метод для получения списка категорий.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        try:
            self.get_all_categories()
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get categories: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении категорий'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CategoriesDetailView(APIView, CategoriesController):
    """
    Api класс для работы с конкретными категориями.
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
        operation_summary='Получение конкретной категории',
        operation_description="Получение конкретной категории пользователя",
        tags=['categories'],
        security=["JWT"],
        responses=response_get_category(),
    )
    def get(self, request, pk):
        """
        Метод для получения категории по id.
        :param request:
        :return:
        """

        self.request = request
        self.post_data = request.data
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
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get category: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении категории'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Изменение конкретной категории',
        operation_description="Изменение конкретной категории пользователя",
        tags=['categories'],
        security=["JWT"],
        request_body=requests_create_category(),
        responses=response_get_category(),
    )
    def put(self, request, pk):
        """
        Метод для обновления категории по id.
        :param request:
        :param pk:
        :return:
        """

        self.request = request
        self.post_data = request.data
        self.pk = pk
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.update_obj()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            import traceback
            traceback.print_exc()
            print(f"Error update category: {_error}")
            self.error_data = {
                'error': f'Ошибка при обновлении категории: {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Удаление конкретной категории',
        operation_description="Удаление конкретной категории пользователя",
        tags=['categories'],
        security=["JWT"],
        responses=response_delete_category(),
    )
    def delete(self, request, pk):
        """
        Метод для удаления категории по id.
        :param request:
        :param pk:
        :return:
        """

        self.request = request
        self.post_data = request.data
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
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error delete category: {_error}")
            self.error_data = {
                'error': 'Ошибка при удалении категории'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
