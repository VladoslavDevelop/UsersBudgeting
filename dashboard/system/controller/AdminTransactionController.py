from Core.Controller.BaseController import BaseController
from Core.Filter.Helper import FilterHelper
from transactions.models import Transactions
from transactions.system.entities.TransactionEntities import TransactionEntities
from transactions.system.serializer.TransactionSeralizer import TransactionSerializer


class AdminTransactionController(BaseController):
    """
    Контроллер для работы с транзакциями.
    """

    obj = None
    request = None
    initial_filters = {}
    filters = None
    limit = 10
    offset = 0
    queryset = None
    all_count = None
    pk = None
    budgeting_total_spend = False

    def get_all_transactions(self):
        """
        Получение всех транзакций.
        :return:
        """
        query_search = self.post_data.get('q', None)

        if query_search:
            query_filters = {
                'or_group': [
                    {'uuid': ['i~', query_search]},
                    {'category__name': ['i~', query_search]},
                    {'type': ['i~', query_search]}
                ]
            }
            self.initial_filters.update(query_filters)

        self.filters = self.post_data.get('filters', {})
        self.initial_filters.update(self.filters)
        self.limit = int(self.post_data.get('limit', 10))
        self.offset = int(self.post_data.get('offset', 0))

        self.get_list()
        self.serializer_data = []
        for obj in self.queryset:
            obj_entity = TransactionEntities(obj)
            self.serializer_data.append(TransactionSerializer(obj_entity).serialize())

    def get_list(self):
        """
        Получение списка транзакций.
        :return:
        """

        queryset = Transactions.objects.select_related('user', 'category').order_by('-id')
        self.filters = FilterHelper(queryset, self.initial_filters)
        self.queryset = self.filters.apply_filters()
        self.all_count = self.queryset.count()
        self.queryset = self.queryset[self.offset:self.limit]

    def get_obj(self):
        """
        Получение транзакции по id.
        :return:
        """

        if self.pk is None:
            self.error_data["error"] = "Не указан id транзакции"
            return
        self.obj = Transactions.objects.filter(
            id=self.pk,
        ).first()

        if self.obj is None:
            self.error_data["error"] = "Транзакция не найдена"
            return

        obj_entity = TransactionEntities(self.obj)
        self.serializer_data = TransactionSerializer(obj_entity).serialize()
