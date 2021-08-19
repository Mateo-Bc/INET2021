from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.HomeView, name="homeView"),
    path('local/<int:pk>', views.Local_View, name="local_view"),
    path('statistics/<int:pk>', views.Statistics_View, name="statistics_view")
]