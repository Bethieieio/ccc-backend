from django.urls import path
from favourites import views

urlpatterns = [
    path('likes/', views.FavouriteList.as_view()),
    path('likes/<int:pk>/', views.FavouriteDetails.as_view()),
]