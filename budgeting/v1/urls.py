from django.urls import path

from budgeting.v1.views import *

urlpatterns = [
    path('', BudgetingView.as_view()),
    path('<int:pk>/', BudgetingDetailView.as_view()),
]
