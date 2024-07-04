from Core.Controller.BaseController import BaseController

from datetime import datetime

from django.db.models import Sum, Q

from reports_and_analytics.system.entities.ReportAnalyticEntities import ReportEntities
from transactions.models import Transactions
from transactions.system.serializer.TransactionSeralizer import TransactionSerializer


class AdminReportAnalyticController(BaseController):
    """
    Контроллер для работы с отчетами и аналитикой.
    """

    category_obj = None
    transaction_obj = None
    budgeting_obj = None
    request = None
    initial_filters = None
    filters = None
    limit = 10
    offset = 0
    queryset = None
    all_count = None
    error_data = {}

    def get_reports(self):
        """
        Получение отчета.
        :return:
        """

        start = self.request.GET.get('start')
        end = self.request.GET.get('end')

        if not start or not end:
            self.error_data = {'error': 'Не указан период отчета'}

        if isinstance(start, datetime) and isinstance(end, datetime):
            date_in = start.combine(start.date(), start.min.time())
            date_out = end.combine(end.date(), end.max.time())
        else:
            date_in = datetime.fromisoformat(start)
            date_out = datetime.fromisoformat(end)
            date_in = date_in.combine(date_in.date(), date_in.min.time())
            date_out = date_out.combine(date_out.date(), date_out.max.time())

        self.queryset = Transactions.objects.filter(
            created_at__range=(date_in, date_out),
            user_id=self.post_data.get('user_id')
        )

        self.serializer_data = []

        for item in self.queryset:
            obj_entity = ReportEntities(item)
            self.serializer_data.append(TransactionSerializer(obj_entity).serialize())

        self.serializer_data = sorted(self.serializer_data, key=lambda x: x['created_at'], reverse=True)

    def get_analytic_category(self):
        """
        Получение аналитики по категории.
        :return:
        """

        start = self.request.GET.get('start')
        end = self.request.GET.get('end')

        if not start or not end:
            self.error_data = {'error': 'Не указан период отчета'}

        if isinstance(start, datetime) and isinstance(end, datetime):
            date_in = start.combine(start.date(), start.min.time())
            date_out = end.combine(end.date(), end.max.time())
        else:
            date_in = datetime.fromisoformat(start)
            date_out = datetime.fromisoformat(end)
            date_in = date_in.combine(date_in.date(), date_in.min.time())
            date_out = date_out.combine(date_out.date(), date_out.max.time())

        transactions = Transactions.objects.filter(
            created_at__range=(date_in, date_out),
            user_id=self.post_data.get('user_id')
        )

        category_data = transactions.values('category__name').annotate(
            total_amount=Sum('amount'),
            total_income=Sum('amount', filter=Q(type='income')),
            total_expense=Sum('amount', filter=Q(type='expense'))
        ).order_by('-total_amount')

        analytics_data = []

        for data in category_data:
            category_name = data['category__name']
            total_amount = data['total_amount']
            total_income = data['total_income'] or 0
            total_expense = data['total_expense'] or 0
            analytics_data.append({
                'category': category_name,
                'total_amount': total_amount,
                'total_income': total_income,
                'total_expense': total_expense
            })

        self.serializer_data = analytics_data
