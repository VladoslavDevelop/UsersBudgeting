from drf_yasg import openapi

api_info = openapi.Info(
    title="API документация к тестовому заданию",
    default_version='v1',
    description="В данной документации представлены примеры запросов и ответов от сервера",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="developperm1613@gmail.com"),
    license=openapi.License(name="MIT License"),
)
