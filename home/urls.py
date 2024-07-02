from . import views
from django.urls import path

urlpatterns = [
    path('t/', views.home)
]