from django.urls import path, include
from articles import views


urlpatterns = [
    path('', views.home, name='home'),
]

