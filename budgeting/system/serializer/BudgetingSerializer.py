from Core.Serializer.BaseSerializer import BaseSerializer


class BudgetingSerializer(BaseSerializer):
    """
    Сериализация бюджета.
    """

    fields = [
        'id',
        'user_obj',
        'category_obj',
        'amount_budgeting',
        'total_spent',
        'is_active',
    ]

    def __init__(self, entity):
        super().__init__(entity)
