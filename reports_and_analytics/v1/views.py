import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from reports_and_analytics.system.controller.ReportAnalyticController import ReportAnalyticController


@permission_classes([IsAuthenticated])
class ReportsView(APIView, ReportAnalyticController):
    """
    Получение отчетов.
    """

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


@permission_classes([IsAuthenticated])
class AnalyticsCategoryView(APIView, ReportAnalyticController):
    """
    Получение аналитики по категории.
    """

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