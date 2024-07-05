from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API документация к тестовому заданию",
        default_version='v1',
        description="В данной документации представлены примеры запросов и ответов от сервера",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="developperm1613@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.v1.urls')),
    path('api/categories/', include('categories.v1.urls')),
    path('api/transactions/', include('transactions.v1.urls')),
    path('api/budgeting/', include('budgeting.v1.urls')),
    path('api/reports/', include('reports_and_analytics.v1.urls')),
    path('api/analytics/', include('reports_and_analytics.v1.urls')),
    path('api/dashboard/', include('dashboard.v1.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
