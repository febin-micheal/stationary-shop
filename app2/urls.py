from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.home, name='home'),
]
