from Core.Controller.BaseController import BaseController
from Core.Filter.Helper import FilterHelper
from users.models import User
from users.system.entities.UserEntities import UserEntitiesShort
from users.system.serializer.UserSerializer import UserProfileSerializer


class AdminUserController(BaseController):
    """
    Контроллер для работы с категориями.
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


    def get_all_users(self):
        """
        Получение всех категорий.
        :return:
        """
        query_search = self.post_data.get('q', None)

        if query_search:
            query_filters = {
                'or_group': [
                    {'username': ['i~', query_search]},
                    {'email': ['i~', query_search]},
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
            obj_entity = UserEntitiesShort(obj)
            self.serializer_data.append(UserProfileSerializer(obj_entity).serialize())

    def get_list(self):
        """
        Получение списка категорий.
        :return:
        """

        queryset = User.objects.order_by('-id')
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
                user = User.objects.get(id=self.pk)
            except:
                self.error_data["error"] = "Категория не найдена"
                return

            obj_entity = UserEntitiesShort(user)
            self.serializer_data = UserProfileSerializer(obj_entity).serialize()
