
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from mantentubike.views import * 


urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password_reset_form/', views.password_reset_form, name='password_reset_form'), 
]
