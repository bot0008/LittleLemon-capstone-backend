from django.contrib import admin 
from django.urls import path, include
from .views import sayHello
from . import views 
from djoser.views import TokenCreateView, TokenDestroyView
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'), 
    path('index/', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/menu-items/', views.MenuItemsView.as_view(), name='items'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
]