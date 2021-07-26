from django.urls import path
from .views import index, login, register, RegisterUser

urlpatterns = [
    path('', index),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register')
]