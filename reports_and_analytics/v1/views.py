import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from reports_and_analytics.system.controller.ReportAnalyticController import ReportAnalyticController
from users.utils import JWTAuthentication


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ReportsView(APIView, ReportAnalyticController):
    """
    Получение отчетов.
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

    def get(self, request):
        """
        Получение отчетов.
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
            self.get_reports()
            if self.error_data:
                return Response(self.error_data, status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при получении отчетов - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class AnalyticsCategoryView(APIView, ReportAnalyticController):
    """
    Получение аналитики по категории.
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

    def get(self, request):
        """
        Получение аналитики.
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
            self.get_analytic_category()
            if self.error_data:
                return Response(self.error_data, status=status.HTTP_400_BAD_REQUEST)
            return Response(self.serializer_data, status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при получении отчетов - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)