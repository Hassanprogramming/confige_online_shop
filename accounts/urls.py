from django.urls import path
from . import views

urlpatterns = [
    path('Registration/', views.Registration, name="registration"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]