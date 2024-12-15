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
#from django.urls import path, include

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
 #path('add-book/', views.add_book, name='add_book'),
 path('simple/query', views.simple_query, name='simple_query'),
 path('complex/query', views.lookup_query, name='lookup_query'),
 path('lab8/task1', views.task1_view, name='task1_view'),
 path('lab8/task2', views.task2_view, name='task2_view'),
 path('lab8/task3', views.task3_view, name='task3_view'),
 path('lab8/task4', views.task4_view, name='task4_view'),
 path('lab8/task5', views.task5_view, name='task5_view'),
 path('students/city_count', views.city_count_view, name='city_count_view'),
 path('lab9_part1/listbooks', views.list_books, name='list_books'),
 path('lab9_part1/addbook', views.add_book, name='add_book'),
 path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
 path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),

 path('lab9_part2/listbooks', views.list_books, name='list_books_form'),
 path('lab9_part2/addbook', views.add_book, name='add_book_form'),
 path('lab9_part2/editbook/<int:id>', views.edit_book, name='edit_book_form'),
 path('lab9_part2/deletebook/<int:id>', views.delete_book, name='delete_book_form'),
 path('', views.list_students, name='list_students'),
 path('add/', views.add_student, name='add_student'),
path('update/<int:pk>/', views.update_student, name='update_student'),
path('delete/<int:pk>/', views.delete_student, name='delete_student'),


path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.list_images, name='list_images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



