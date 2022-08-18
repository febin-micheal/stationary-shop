from typing import ItemsView
from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('store/', views.store, name='store'),
    # path('store/<pk>', views.store, name='store'),
    # path('item/', views.item, name='item'),
    # path('item/<pk>', views.item, name='item'),
    path('store/', views.StoreView.as_view(), name='store'),
    path('store/<pk>', views.StoreView.as_view(), name='store'),
    path('item/', views.ItemView.as_view(), name='item'),
    path('item/<pk>', views.ItemView.as_view(), name='item'),
]
