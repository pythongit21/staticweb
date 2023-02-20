from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('loginp', views.loginp, name='login'),
    path('logoutp', views.logoutp, name='logout')
]
