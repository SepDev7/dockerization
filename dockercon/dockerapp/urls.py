from django.urls import path
from dockerapp import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
