from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("loginpage", views.loginpage, name='loginpage'),
    path("login", views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name='contact'), 
    path("signup", views.handleSignUp, name='signup'), 
    path('search', views.search, name='search')
]