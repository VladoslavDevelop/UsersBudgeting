import base64
import hashlib

import jwt
from django.conf import settings
from rest_framework import authentication, exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    """
    Класс для авторизации через JWT токен.
    """

    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """
        Авторизация пользователя.
        :param request:
        :return:
        """

        request.user = None
        request.type_access = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            return None
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Данные для авторизации.
        :param token:
        :return:
        """
        from .models import User
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception as e:
            raise exceptions.AuthenticationFailed(e)

        try:
            pk = payload['user_id']
            user = User.objects.get(pk=pk)
        except Exception as _error:
            msg = 'Пользователь соответствующий данному токену не найден.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'Данный пользователь деактивирован.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)

    def decode(self, uuid):
        decoded_user_id = base64.b64decode(uuid.encode()).decode()
        return int(decoded_user_id)

    def create_hash(self, updated_at):
        return hashlib.sha256(str(updated_at).encode()).hexdigest()
