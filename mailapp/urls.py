from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailfunction, name="mailfunction"),
]
