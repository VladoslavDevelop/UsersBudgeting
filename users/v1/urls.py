from django.urls import path

from users.v1.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
