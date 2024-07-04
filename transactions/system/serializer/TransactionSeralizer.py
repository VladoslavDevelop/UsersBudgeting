from Core.Serializer.BaseSerializer import BaseSerializer


class TransactionSerializer(BaseSerializer):
    """
    Сериализация транзакций.
    """

    fields = [
        'id',
        'uuid',
        'user_obj',
        'category_obj',
        'type',
        'amount',
        'description',
        'created_at',
        'is_active',
        'attention_msg'
    ]

    def __init__(self, entity):
        super().__init__(entity)
