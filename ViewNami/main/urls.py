from django.urls import path
from main.views import index
from . import views 

urlpatterns = [
    path('animes', views.index)
]