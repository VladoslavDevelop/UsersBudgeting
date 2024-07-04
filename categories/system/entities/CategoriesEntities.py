from Core.Entity.BaseEntity import BaseEntity
from users.system.entities.UserEntities import UserEntitiesShort
from users.system.serializer.UserSerializer import UserShortSerializer


class CategoriesEntities(BaseEntity):
    """
    Сущность для работы с категориями.
    """

    def __init__(self, model_instance):
        super().__init__(model_instance)

    def id(self):
        return self.model_instance.id

    def name(self):
        return self.model_instance.name

    def user_obj(self):
        obj_entities = UserEntitiesShort(self.model_instance.user)

        return UserShortSerializer(obj_entities).serialize()


class CategoryEntitiesShort(BaseEntity):
    """
    Сокращенная сущность для работы с категориями.
    """

    def __init__(self, model_instance):
        super().__init__(model_instance)

    def id(self):
        return self.model_instance.id

    def name(self):
        return self.model_instance.name
