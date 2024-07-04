from Core.Serializer.BaseSerializer import BaseSerializer


class ReportSerializer(BaseSerializer):
    """
    Сериализация отчетов.
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
        'is_active'
    ]

    def __init__(self, entity):
        super().__init__(entity)


class AnalyticCategorySerializer(BaseSerializer):
    """
    Сериализация аналитики по категориям.
    """

    fields = [

    ]

    def __init__(self, entity):
        super().__init__(entity)