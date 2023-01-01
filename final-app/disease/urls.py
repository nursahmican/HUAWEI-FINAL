
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('index/', views.index, name="home"),
    path('results/', views.results, name="results"),
    path('result/<str:pk>/', views.result, name="result"),

]
