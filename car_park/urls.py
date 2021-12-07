from django.urls import path

from car_park import views

urlpatterns = [
    path('', views.home, name='home_page'),
]
