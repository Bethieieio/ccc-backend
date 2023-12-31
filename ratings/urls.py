"""rating urls"""
from django.urls import path
from ratings import views

urlpatterns = [
    path('ratings/', views.RatingList.as_view()),
    path('ratings/<int:pk>/', views.RatingDetails.as_view()),
]
