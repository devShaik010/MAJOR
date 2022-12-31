from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('signup/',sign_up),
    path('product/',product),
    path('book/',book),
    path('login/',login)

]
