from django.urls import path
from app2 import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/<pk>', views.store, name='store'),
    path('item/', views.item, name='item'),
    path('item/<pk>', views.item, name='item'),
]
