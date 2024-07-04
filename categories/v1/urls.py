from django.urls import path

from categories.v1.views import *

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:pk>/', CategoriesDetailView.as_view()),
]
