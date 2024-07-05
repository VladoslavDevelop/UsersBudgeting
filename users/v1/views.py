import traceback

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.documentation import *
from users.system.controller.UserController import UserController
from users.utils import JWTAuthentication


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

    @swagger_auto_schema(
        operation_summary='Регистрация',
        operation_description="Регистрация нового пользователя",
        tags=['users'],
        security=[],
        request_body=request_registration(),
        responses=response_registration()
    )
    def post(self, request):
        self.post_data = request.data
        self.is_create = True
        self.validate_parameters(request)
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.create_user()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_201_CREATED)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при создании пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
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

    @swagger_auto_schema(
        operation_summary='Авторизация',
        operation_description="Авторизация пользователя",
        tags=['users'],
        security=[],
        request_body=request_login(),
        responses=response_login()
    )
    def post(self, request):
        self.post_data = request.data
        self.validate_parameters(request)
        self.search_is_email = True
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.login_user()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': 'Ошибка при авторизации пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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

    @swagger_auto_schema(
        operation_summary='Выход',
        operation_description="Выход из аккаунта пользователя",
        tags=['users'],
        security=["JWT"],
        responses=response_login()
    )
    def post(self, request):
        self.post_data = request.data
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.is_request = True
        self.validate_parameters(request)
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.logout_user()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            self.error_data = {
                'error': f'Ошибка при выходе пользователя - {_error}'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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

    @swagger_auto_schema(
        operation_summary='Профиль пользователя',
        operation_description="Получение информации пользователя",
        tags=['users'],
        security=[{'Token': []}],
        responses=response_profile()
    )
    def get(self, request):
        self.is_request = True
        self.validate_parameters(request)
        self.token = request.META.get('HTTP_AUTHORIZATION')
        self.check_available_token()
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.get_user()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            traceback.print_exc()
            print(f"Error get user: {_error}")
            self.error_data = {
                'error': 'Ошибка при получении пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Изменение профиля',
        operation_description="Изменение информации профиля пользователя",
        tags=['users'],
        security=[{'Token': []}],
        request_body=requests_update_profile(),
        responses=response_profile()
    )
    def put(self, request):
        self.post_data = request.data
        self.is_request = True
        self.validate_parameters(request)
        if self.error_data:
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
        try:
            self.update_user()
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            print(f"Error update user: {_error}")
            self.error_data = {
                'error': 'Ошибка при обновлении пользователя'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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

    @swagger_auto_schema(
        operation_summary='Обновление токена',
        operation_description="Получение нового токена",
        tags=['users'],
        security=["JWT"],
        responses=response_login()
    )
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
            if self.error_data:
                return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
            return Response(self.success_response(), status=status.HTTP_200_OK)
        except Exception as _error:
            print(f"Error refresh token: {_error}")
            self.error_data = {
                'error': 'Ошибка при обновлении токена'
            }
            return Response(self.error_response(), status=status.HTTP_400_BAD_REQUEST)
