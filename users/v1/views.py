import traceback

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.system.controller.UserController import UserController


@permission_classes([AllowAny])
class UserRegistrationView(APIView, UserController):
    """
    Класс для регистрации пользователя.
    """

    _required_parameters = ['email', 'password', 'password_confirm']
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        self.post_data = request.data
        self.is_create = True
        self.validate_parameters(request)
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.create_user()
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при создании пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView, UserController):
    """
    Класс для авторизации пользователя.
    """

    _required_parameters = ['email', 'password']
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        self.post_data = request.data
        self.validate_parameters(request)
        self.search_is_email = True
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.login_user()
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при авторизации пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView, UserController):
    """
    Класс для выхода пользователя.
    """

    _required_parameters = []
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        self.post_data = request.data
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.is_request = True
        self.validate_parameters(request)
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.logout_user()
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при выходе пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView, UserController):
    _required_parameters = []
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def get(self, request):
        self.is_request = True
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_user()
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            print(f"Error get user: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        self.post_data = request.data
        self.is_request = True
        self.validate_parameters(request)
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.update_user()
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            print(f"Error update user: {_error}")
            self.error_data = {
                'error': 'Ошибка при обновлении пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


class TokenRefreshView(APIView, UserController):
    _required_parameters = []
    _default_message = {
        'errors': {
            'field_not_provided': {
                'en': 'Field {field_name} not provided',
                'ru': 'Поле {field_name} не предоставлено'
            }
        }
    }

    def post(self, request):
        self.post_data = request.data
        self.is_request = True
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.refresh_token()
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            print(f"Error refresh token: {_error}")
            self.error_data = {
                'error': 'Ошибка при обновлении токена'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
