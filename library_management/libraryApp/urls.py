from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('readers/', views.readers, name='readers'),
    path('edit_reader/<int:reader_id>/', views.edit_reader, name='edit_reader'),
    path('books/', views.books, name='books'),
    path('add_to_bag/<int:book_id>/', views.add_to_bag, name='add_to_bag'),
    path('bag/', views.bag, name='bag'),
    path('return_book_page/', views.return_book_page, name='return_book_page'),
    path('return_book/<int:borrow_id>/', views.return_book, name='return_book'),
]