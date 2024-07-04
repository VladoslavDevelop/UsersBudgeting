from django.urls import path

from dashboard.v1.views import *

urlpatterns = [
    # category
    path('category/all/', CategoryAllView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    # transaction
    path('transaction/all/', TransactionAllView.as_view()),
    path('transaction/<int:pk>/', TransactionDetailView.as_view()),

    # budget
    path('budget/all/', BudgetAllView.as_view()),
    path('budget/<int:pk>/', BudgetDetailView.as_view()),

    # user
    path('user/all/', UserAllView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),

    # reports
    path('reports/', ReportsAllView.as_view()),

    # analytics
    path('analytics/', AnalyticsAllView.as_view()),
]