from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="recipes-home") , # home
    path('recipes/<int:id>/', views.recipes, name="recipes-recipe") , # home
]