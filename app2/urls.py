from typing import ItemsView
from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.StoreView.as_view(), name='store_list'),
    path('store/create/', views.StoreView.as_view(), name='store_create'),
    path('store/update/<pk>', views.StoreView.as_view(), name='store_update'),
    path('store/delete/<pk>', views.StoreView.as_view(), name='store_delete'),
    path('item/', views.ItemView.as_view(), name='item_list'),
    path('item/create/', views.ItemView.as_view(), name='item_create'),
    path('item/update/<pk>', views.ItemView.as_view(), name='item_update'),
    path('item/delete/<pk>', views.ItemView.as_view(), name='item_delete'),
]
