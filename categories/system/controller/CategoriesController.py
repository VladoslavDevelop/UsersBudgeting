from Core.Controller.BaseController import BaseController
from Core.Filter.Helper import FilterHelper
from categories.models import Categories
from categories.system.entities.CategoriesEntities import CategoriesEntities
from categories.system.serializer.CategoriesSerializer import CategoriesSerializer


class CategoriesController(BaseController):
    """
    Контроллер для работы с категориями.
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

    def create_obj(self):
        """
        Создание объекта категории.
        :return:
        """

        if self.request.user is None:
            self.error_data["error"] = "Пользователь не найден"
            return

        if 'name' not in self.post_data:
            self.error_data["error"] = "Поле 'name' обязательно"
            return

        if Categories.objects.filter(
            name=self.post_data.get('name'),
            user=self.request.user
        ).exists():
            self.error_data["error"] = "Категория с таким именем уже существует"
            return

        self.obj = Categories.objects.create(
            name=self.post_data.get('name'),
            user=self.request.user
        )

        obj_entity = CategoriesEntities(self.obj)
        self.serializer_data = CategoriesSerializer(obj_entity).serialize()

    def get_all_categories(self):
        """
        Получение всех категорий.
        :return:
        """

        self.initial_filters = {
            'user': ['=', self.request.user],
            'is_active': ['=', 'True']
        }
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
        self.limit = self.post_data.get('limit', 10)
        self.offset = self.post_data.get('offset', 0)
        self.get_list()
        self.serializer_data = []
        for obj in self.queryset:
            obj_entity = CategoriesEntities(obj)
            self.serializer_data.append(CategoriesSerializer(obj_entity).serialize())

    def get_list(self):
        """
        Получение списка категорий.
        :return:
        """

        queryset = Categories.objects.select_related('user').order_by('id')
        self.filters = FilterHelper(queryset, self.initial_filters)
        self.queryset = self.filters.apply_filters()
        self.all_count = self.queryset.count()
        self.queryset = self.queryset[self.offset:self.limit]

    def get_obj(self):
        """
        Получение объекта категории.
        :return:
        """

        if self.pk is not None:
            try:
                category = Categories.objects.get(id=self.pk)
            except Categories.DoesNotExist:
                self.error_data["error"] = "Категория не найдена"
                return

            if self.request.user != category.user:
                self.error_data["error"] = "Вы не можете получить категорию другого пользователя"

            obj_entity = CategoriesEntities(category)
            self.serializer_data = CategoriesSerializer(obj_entity).serialize()

    def update_obj(self):
        """
        Обновление объекта категории.
        :return:
        """

        if self.pk is not None:
            try:
                category = Categories.objects.get(id=self.pk)
            except:
                self.error_data["error"] = "Категория не найдена"
                return

            if self.request.user != category.user:
                self.error_data["error"] = "Вы не можете обновить категорию другого пользователя"
                return

            if 'name' not in self.post_data and 'is_active' not in self.post_data:
                self.error_data["error"] = "Должно быть передано хотя бы одно из полей: name или is_active"
                return

            if 'user' in self.post_data:
                self.error_data["error"] = "Поле 'user' не может быть изменено"
                return

            if 'name' in self.post_data:
                category.name = self.post_data.get('name')
            if 'is_active' in self.post_data:
                category.is_active = self.post_data.get('is_active')

            category.save()

            obj_entity = CategoriesEntities(category)
            self.serializer_data = CategoriesSerializer(obj_entity).serialize()

    def delete_obj(self):
        """
        Удаление объекта категории.
        :return:
        """

        if self.pk is not None:
            try:
                self.obj = Categories.objects.get(id=self.pk)
            except:
                self.error_data["error"] = "Категория не найдена"
                return

            if self.request.user != self.obj.user:
                self.error_data["error"] = "Вы не можете удалить категорию другого пользователя"
                return

            self.obj.is_active = False
            self.obj.save()

            obj_entity = CategoriesEntities(self.obj)
            self.serializer_data = CategoriesSerializer(obj_entity).serialize()
