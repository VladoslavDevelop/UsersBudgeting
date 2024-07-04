from Core.Serializer.BaseSerializer import BaseSerializer


class CategoriesSerializer(BaseSerializer):
    """
    Сериализация категорий.
    """

    fields = [
        'id',
        'name',
        'user_obj',
        'is_active'
    ]

    def __init__(self, entity):
        super().__init__(entity)


class CategoriesShortSerializer(BaseSerializer):
    """
    Сериализация сокращенной категории.
    """

    fields = [
        'id',
        'name'
    ]

    def __init__(self, entity):
        super().__init__(entity)