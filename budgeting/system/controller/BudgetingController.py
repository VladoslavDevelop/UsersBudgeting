from Core.Controller.BaseController import BaseController
from Core.Filter.Helper import FilterHelper
from budgeting.models import BudgetingCategories
from budgeting.system.entities.BudgetingEntities import BudgetingEntities
from budgeting.system.serializer.BudgetingSerializer import BudgetingSerializer
from categories.models import Categories


class BudgetingController(BaseController):
    """
    Контроллер для работы с бюджетами.
    """

    obj = None
    request = None
    initial_filters = None
    filters = None
    limit = 10
    offset = 0
    queryset = None
    all_count = None
    pk = None
    error_data = {}

    def create_budgeting(self):
        """
        Создание бюджета.
        :return:
        """

        required_fields = [
            'category_id',
            'amount_budgeting',
        ]

        if self.request.user is None:
            self.error_data["error"] = "Пользователь не найден"
            return

        missing_fields = [field for field in required_fields if field not in self.post_data]
        if missing_fields:
            self.error_data["error"] = f"Не все поля заполнены. Отсутствуют: {', '.join(missing_fields)}"
            return

        category = Categories.objects.filter(
            id=self.post_data.get('category_id'),
            user=self.request.user,
            is_active=True
        )
        if not category.exists():
            self.error_data["error"] = "Категория не найдена"
            return

        if BudgetingCategories.objects.filter(
            category=category.first(),
            user=self.request.user,
        ).exists():
            self.error_data["error"] = "Бюджет для данной категории установлен"
            return

        self.obj = BudgetingCategories.objects.create(
            category=category.first(),
            amount_budgeting=self.post_data.get('amount_budgeting'),
            user=self.request.user,
        )

        obj_entity = BudgetingEntities(self.obj)
        self.serializer_data = BudgetingSerializer(obj_entity).serialize()

    def get_budgeting_all(self):
        """
        Получение всех бюджетов.
        :return:
        """

        self.initial_filters = {
            'user': ['=', self.request.user],
            'is_active': ['=', True]
        }
        query_search = self.post_data.get('q', None)

        if query_search:
            query_filters = {
                'or_group': [
                    {'category__name': ['i~', query_search]},
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
            user=self.request.user,
            is_active=True
        )
        if not self.obj.exists():
            self.error_data["error"] = "Бюджет не найден"
            return

        obj_entity = BudgetingEntities(self.obj.first())
        self.serializer_data = BudgetingSerializer(obj_entity).serialize()

    def update_budgeting(self):
        """
        Обновление бюджета.
        :return:
        """

        if self.request.user is None:
            self.error_data["error"] = "Пользователь не найден"
            return

        self.obj = BudgetingCategories.objects.filter(
            id=self.pk,
            user=self.request.user,
            is_active=True
        )
        if not self.obj.exists():
            self.error_data["error"] = "Бюджет не найден"
            return

        if 'category_id' in self.post_data:
            category = Categories.objects.filter(
                id=self.post_data.get('category_id'),
                user=self.request.user,
                is_active=True
            )
            if not category.exists():
                self.error_data["error"] = "Категория не найдена"
                return

            self.obj.update(
                category=category.first()
            )

        self.obj.update(
            amount_budgeting=self.post_data.get('amount_budgeting', self.obj.first().amount_budgeting)
        )

        obj_entity = BudgetingEntities(self.obj.first())
        self.serializer_data = BudgetingSerializer(obj_entity).serialize()

    def delete_budgeting(self):
        """
        Удаление бюджета.
        :return:
        """

        self.obj = BudgetingCategories.objects.filter(
            id=self.pk,
            user=self.request.user,
            is_active=True
        )
        if not self.obj.exists():
            self.error_data["error"] = "Бюджет не найден"
            return

        self.obj.update(
            is_active=False
        )
        obj_entity = BudgetingEntities(self.obj.first())
        self.serializer_data = BudgetingSerializer(obj_entity).serialize()

