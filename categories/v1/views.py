import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from categories.system.controller.CategoriesController import CategoriesController


@permission_classes([IsAuthenticated])
class CategoriesView(APIView, CategoriesController):
    """
    Api класс для работы с категориями.
    """

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
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error create category: {_error}")
            self.error_data = {
                'error': 'Ошибка при создании категории'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

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


class CategoriesDetailView(APIView, CategoriesController):
    """
    Api класс для работы с конкретными категориями.
    """

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