from Core.Entity.BaseEntity import BaseEntity
from budgeting.models import BudgetingCategories
from users.system.entities.UserEntities import UserEntitiesShort
from users.system.serializer.UserSerializer import UserShortSerializer
from categories.system.serializer.CategoriesSerializer import CategoriesShortSerializer
from categories.system.entities.CategoriesEntities import CategoryEntitiesShort


class TransactionEntities(BaseEntity):
    """
    Сущность для работы с транзакциями.
    """

    def __init__(self, model_instance):
        super().__init__(model_instance)

    def id(self):
        return self.model_instance.id

    def category_obj(self):
        obj_entities = CategoryEntitiesShort(self.model_instance.category)

        return CategoriesShortSerializer(obj_entities).serialize()

    def date(self):
        return self.model_instance.date

    def description(self):
        return self.model_instance.description

    def user_obj(self):
        obj_entities = UserEntitiesShort(self.model_instance.user)

        return UserShortSerializer(obj_entities).serialize()

    def attention_msg(self):
        budgeting = BudgetingCategories.objects.select_related(
            "category",
            "user"
        ).filter(
            user=self.model_instance.user,
            category=self.model_instance.category
        )
        if budgeting.exists():
            budgeting = budgeting.first()
            transaction_amount = self.model_instance.amount
            total_spent = budgeting.total_spent
            budgeting_amount = budgeting.amount_budgeting
            amount_exceeding = self.model_instance.user.amount_exceeding

            remaining_budget = budgeting_amount - total_spent

            if remaining_budget - transaction_amount <= amount_exceeding:
                return True

        return False



