from django.urls import path
from .views import (
    index, logout_user, markup, checkup, RegisterUser, LoginUser,
    upload,check,
)

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('markup/', markup, name='markup'),
    path('checkup/', checkup, name='checkup'),
    path('upload/', upload, name='upload'),
    path('check/', check, name='check'),
]