from django.contrib import admin 
from django.urls import path, include
from .views import sayHello
from . import views 
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 

    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('menu/menu-items/', views.MenuItemsView.as_view(), name='items'),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    
]