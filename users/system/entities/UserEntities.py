from Core.Entity.BaseEntity import BaseEntity


class UserEntities(BaseEntity):
    """
    Сущность для работы с пользователями.
    """

    def __init__(self, model_instance):
        super().__init__(model_instance)

    def id(self):
        return self.model_instance.id

    def email(self):
        return self.model_instance.email

    def token(self):
        return self.model_instance.token


class UserEntitiesShort(BaseEntity):
    """
    Сокращенная сущность для работы с пользователями.
    """

    def __init__(self, model_instance):
        super().__init__(model_instance)

    def id(self):
        return self.model_instance.id

    def email(self):
        return self.model_instance.email
