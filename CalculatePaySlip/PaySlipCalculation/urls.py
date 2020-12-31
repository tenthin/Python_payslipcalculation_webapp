from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='home'),
    path('calculate', views.calculate, name='calculate'),
    path('reset', views.reset, name='reset')
]
