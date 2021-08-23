from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.HomeView, name="homeView"),
    path('statistics/', views.Statistics_View, name="statistics_view"),
    path('local/<int:pk>', views.Local_View, name="local_view"),
    

    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]