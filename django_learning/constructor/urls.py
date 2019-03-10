from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.constructor, name='test_func'),
]
