from decimal import Decimal

from Core.Controller.BaseController import BaseController
from Core.Filter.Helper import FilterHelper
from Core.Utils.Generate import Generate
from budgeting.models import BudgetingCategories
from categories.models import Categories
from transactions.models import Transactions
from transactions.system.entities.TransactionEntities import TransactionEntities
from transactions.system.serializer.TransactionSeralizer import TransactionSerializer


class TransactionController(BaseController):
    """
    Контроллер для работы с транзакциями.
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
    budgeting_total_spend = False

    def create_obj(self):
        """
        Создание объекта транзакции.
        :return:
        """

        required_fields = [
            'category_id',
            'amount',
            'type'
        ]

        if self.request.user is None:
            self.error_data["error"] = "Пользователь не найден"
            return

        missing_fields = [field for field in required_fields if field not in self.post_data]
        if missing_fields:
            self.error_data["error"] = f"Не все поля заполнены. Отсутствуют: {', '.join(missing_fields)}"
            return

        uuid = Generate(count=16).generate()

        while Transactions.objects.filter(uuid=uuid).exists():
            uuid = Generate(count=16).generate()

        category = Categories.objects.filter(
            id=self.post_data.get('category_id'),
            user=self.request.user,
            is_active=True
        )
        if not category.exists():
            self.error_data["error"] = "Категория не найдена"
            return

        budgeting_search = BudgetingCategories.objects.filter(
            category=category.first(),
            user=self.request.user,
            is_active=True
        )
        if budgeting_search.exists():
            budgeting = budgeting_search.first()
            budgeting.total_spent += Decimal(self.post_data.get('amount'))
            budgeting.save()
            if budgeting.total_spent > budgeting.amount_budgeting:
                self.budgeting_total_spend = True

        self.obj = Transactions.objects.create(
            category=category.first(),
            amount=self.post_data.get('amount'),
            type=self.post_data.get('type'),
            user=self.request.user,
            uuid=uuid
        )

        obj_entity = TransactionEntities(self.obj)
        self.serializer_data = TransactionSerializer(obj_entity).serialize()
        if self.budgeting_total_spend:
            self.serializer_data['attention'] = 'Внимание! Бюджет по выбранной категории превышен !'

    def get_all_transactions(self):
        """
        Получение всех транзакций.
        :return:
        """

        self.initial_filters = {
            'user': ['=', self.request.user],
        }
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

        if self.request.user is None:
            self.error_data["error"] = "Пользователь не найден"
            return

        self.obj = Transactions.objects.filter(
            id=self.pk,
            user=self.request.user
        ).first()

        if self.obj is None:
            self.error_data["error"] = "Транзакция не найдена"
            return

        obj_entity = TransactionEntities(self.obj)
        self.serializer_data = TransactionSerializer(obj_entity).serialize()

    def update_obj(self):
        """
        Обновление транзакции по id.
        :return:
        """
        if self.pk is None:
            self.error_data["error"] = "Не указан id транзакции"
            return

        if self.request.user is None:
            self.error_data["error"] = "Пользователь не найден"
            return

        self.obj = Transactions.objects.filter(
            id=self.pk,
            user=self.request.user
        ).first()

        if self.obj is None:
            self.error_data["error"] = "Транзакция не найдена"
            return

        self.obj.amount = self.post_data.get('amount', self.obj.amount)
        self.obj.type = self.post_data.get('type', self.obj.type)
        self.obj.category_id = self.post_data.get('category_id', self.obj.category_id)

        self.obj.save()

        obj_entity = TransactionEntities(self.obj)
        self.serializer_data = TransactionSerializer(obj_entity).serialize()

    def delete_obj(self):
        """
        Удаление транзакции по id.
        :return:
        """

        if self.pk is not None:
            try:
                self.obj = Transactions.objects.get(id=self.pk)
            except:
                self.error_data["error"] = "Транзакция не найдена"
                return

            if self.request.user != self.obj.user:
                self.error_data["error"] = "Вы не можете удалить транзакцию другого пользователя"
                return

            obj_entity = TransactionEntities(self.obj)
            self.serializer_data = TransactionSerializer(obj_entity).serialize()
