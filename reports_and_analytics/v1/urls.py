from django.urls import path

from reports_and_analytics.v1.views import *

urlpatterns = [
    path('', ReportsView.as_view()),
    path('categories/', AnalyticsCategoryView.as_view()),
]
