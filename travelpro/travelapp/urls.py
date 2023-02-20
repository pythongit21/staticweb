from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepg, name='homes')
]