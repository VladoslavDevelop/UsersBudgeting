import re
import traceback

from django.contrib.auth import password_validation

from Core.Controller.BaseController import BaseController

from users.models import User, BlacklistedToken
from users.system.entities.UserEntities import UserEntities, UserEntitiesShort
from users.system.serializer.UserSerializer import *


class UserController(BaseController):
    """
    Контроллер для работы с пользователями.
    """

    obj = None
    payload = None
    is_create = False
    is_request = False
    search_is_email = False
    token = None

    def create_user(self):
        """
        Создание пользователя.
        :return:
        """

        self.generate_payload_user()
        self.create_obj()
        obj_entity = UserEntities(self.obj)
        self.serializer_data = UserSerializer(obj_entity).serialize()

    def generate_payload_user(self):
        self.payload = {
            'username': self.post_data.get('email'),
            'email': self.post_data.get('email'),
            'password': self.post_data.get('password'),
        }

    def create_obj(self):
        """
        Создание объекта пользователя.
        :return:
        """

        self.obj = User.objects.create_user(**self.payload)

    def validate_parameters(self, request):
        """
        Валидация параметров пользователя.
        :param request:
        :return:
        """

        super().validate_parameters(request)
        if self.is_create:
            if self.post_data.get('password') != self.post_data.get('password_confirm'):
                self.error_data['password_confirm'] = 'Пароли не совпадают'
            try:
                password_validation.validate_password(self.post_data.get('password'))
            except Exception as _error:
                traceback.print_exc()
                print(f"Error validation password: {_error}")
                self.error_data['password'] = 'Пароль не соответствует требованиям'
            try:
                User.objects.get(email=self.post_data.get('email'))
                self.error_data['email'] = 'Пользователь с таким email уже существует'
            except User.DoesNotExist:
                pass
            try:
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(pattern, self.post_data.get('email')):
                    self.error_data['email'] = 'Неверный формат email'
            except Exception as _error:
                traceback.print_exc()
                print(f"Error validation email: {_error}")
                self.error_data['email'] = 'Неверный формат email'

    def login_user(self):
        """
        Авторизация пользователя.
        :return:
        """
        self.get_obj()
        self.validate_creds()

        obj_entity = UserEntities(self.obj)
        self.serializer_data = UserAuthSerializer(obj_entity).serialize()

    def get_obj(self):
        """
        Получение объекта пользователя.
        :return:
        """

        if self.is_request:
            self.obj = self.user
        else:
            try:
                if self.search_is_email:
                    self.obj = User.objects.get(email=self.post_data.get('email'))
            except Exception as _error:
                print(f"{_error}")
                self.error_data['not_found'] = 'Пользователь не найден'
                raise ValueError(self.error_data)

    def validate_creds(self):
        """
        Валидация данных пользователя.
        :return:
        """

        if self.obj.is_active is False:
            self.error_data['is_active'] = 'Пользователь не активен'
        if self.obj.check_password(self.post_data.get('password')) is False:
            self.error_data['wrong_password'] = 'Неверный пароль'

    def logout_user(self):
        """
        Выход пользователя.
        :return:
        """
        self.get_obj()

        BlacklistedToken.objects.create(token=self.token)

        obj_entity = UserEntitiesShort(self.obj)
        self.serializer_data = UserShortSerializer(obj_entity).serialize()

    def get_user(self):
        """
        Получение пользователя.
        :return:
        """

        self.get_obj()

        print(f"token {self.obj.token}")
        print(f"activ token {self.obj.is_token_blacklisted(token=self.obj.token)}")

        if self.obj.is_token_blacklisted(
            token=self.obj.token
        ):
            self.error_data['token'] = 'Токен пользователя заблокирован'
            return

        obj_entity = UserEntitiesShort(self.obj)
        self.serializer_data = UserProfileSerializer(obj_entity).serialize()

    def refresh_token(self):
        """
        Обновление токена.
        :return:
        """

        self.get_obj()
        self.obj.token = self.obj.generate_token()
        self.obj.save()

        obj_entity = UserEntities(self.obj)
        self.serializer_data = UserSerializer(obj_entity).serialize()

    def update_user(self):
        """
        Обновление пользователя.
        :return:
        """

        self.get_obj()
        self.obj.username = self.post_data.get('username', self.obj.username)
        self.obj.email = self.post_data.get('email', self.obj.email)
        self.obj.amount_exceeding = self.post_data.get('amount_exceeding', self.obj.amount_exceeding)
        self.obj.save()

        obj_entity = UserEntitiesShort(self.obj)
        self.serializer_data = UserProfileSerializer(obj_entity).serialize()

