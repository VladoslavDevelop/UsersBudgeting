import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from transactions.system.controller.TransactionController import TransactionController


@permission_classes([IsAuthenticated])
class TransactionView(APIView, TransactionController):
    """
    Получение списка транзакций.
    """

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


class TransactionDetailView(APIView, TransactionController):
    """
    Получение конкретной транзакции.
    """

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
