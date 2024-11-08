"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
# path('', views.index),
 #path('index2/<int:val1>/', views.index2),
 #path('<int:bookId>', views.viewbook),


 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  # Updated name
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links_page, name='books.links'),
 path('html5/text/formatting', views.formatting, name='formatting'),
 path('html5/listing', views.listing, name='listing'),
 path('html5/tables', views.tables, name='tables'),
 path('search', views.search, name='search'),


]
