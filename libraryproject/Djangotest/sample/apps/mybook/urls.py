from django import apps
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/',views.book_list,name='book_list'),
    path('books/<int:bID>/', views.book_details, name='book_detail'),
    path('books/<str:name>/',views.index,name='welcome'),
]
