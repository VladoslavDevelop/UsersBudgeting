from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.v1.urls')),
    path('api/categories/', include('categories.v1.urls')),
    path('api/transactions/', include('transactions.v1.urls')),
    path('api/budgeting/', include('budgeting.v1.urls')),
    path('api/reports/', include('reports_and_analytics.v1.urls')),
    path('api/analytics/', include('reports_and_analytics.v1.urls')),

    path('api/dashboard/', include('dashboard.v1.urls')),
]
