import imp
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.front_page, name='frontpage'),
     path('signup/', views.signup, name='signup'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]

