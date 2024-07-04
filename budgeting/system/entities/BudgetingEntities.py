from Core.Entity.BaseEntity import BaseEntity
from users.system.entities.UserEntities import UserEntitiesShort
from users.system.serializer.UserSerializer import UserShortSerializer
from categories.system.serializer.CategoriesSerializer import CategoriesShortSerializer
from categories.system.entities.CategoriesEntities import CategoryEntitiesShort


class BudgetingEntities(BaseEntity):
    """
    Сущность для работы с бюджетом.
    """

    def __init__(self, model_instance):
        super().__init__(model_instance)

    def id(self):
        return self.model_instance.id

    def user_obj(self):
        obj_entities = UserEntitiesShort(self.model_instance.user)

        return UserShortSerializer(obj_entities).serialize()

    def category_obj(self):
        obj_entities = CategoryEntitiesShort(self.model_instance.category)

        return CategoriesShortSerializer(obj_entities).serialize()

    def amount_budgeting(self):
        return self.model_instance.amount

