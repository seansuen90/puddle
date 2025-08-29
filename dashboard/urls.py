
from django.urls import include, path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='index'),

]
  
