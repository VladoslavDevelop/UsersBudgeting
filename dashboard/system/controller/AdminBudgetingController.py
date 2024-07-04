from Core.Controller.BaseController import BaseController
from Core.Filter.Helper import FilterHelper
from budgeting.models import BudgetingCategories
from budgeting.system.entities.BudgetingEntities import BudgetingEntities
from budgeting.system.serializer.BudgetingSerializer import BudgetingSerializer


class AdminBudgetingController(BaseController):
    """
    Контроллер для работы с бюджетами.
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
    error_data = {}

    def get_budgeting_all(self):
        """
        Получение всех бюджетов.
        :return:
        """

        query_search = self.post_data.get('q', None)

        if query_search:
            query_filters = {
                'or_group': [
                    {'name': ['i~', query_search]},
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
            obj_entity = BudgetingEntities(obj)
            self.serializer_data.append(BudgetingSerializer(obj_entity).serialize())

    def get_list(self):
        """
        Получение списка.
        :return:
        """

        queryset = BudgetingCategories.objects.select_related(
            'category',
            'user'
        ).order_by('id')
        self.filters = FilterHelper(queryset, self.initial_filters)
        self.queryset = self.filters.apply_filters()
        self.all_count = self.queryset.count()
        self.queryset = self.queryset[self.offset:self.limit]

    def get_budgeting(self):
        """
        Получение бюджета.
        :return:
        """

        self.obj = BudgetingCategories.objects.filter(
            id=self.pk,
        )
        if not self.obj.exists():
            self.error_data["error"] = "Бюджет не найден"
            return

        obj_entity = BudgetingEntities(self.obj.first())
        self.serializer_data = BudgetingSerializer(obj_entity).serialize()
