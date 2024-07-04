from django.urls import path

from transactions.v1.views import *

urlpatterns = [
    path('', TransactionView.as_view()),
    path('<int:pk>/', TransactionDetailView.as_view()),
]
