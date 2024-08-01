from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('add_to_favorites/<int:item_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:item_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('favorites/', views.view_favorites, name='favorites'),
]