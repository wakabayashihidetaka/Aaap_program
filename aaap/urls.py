from django.urls import path
from . import views

app_name = 'aaap'
urlpatterns = [
    path('', views.index, name='index'),
]
