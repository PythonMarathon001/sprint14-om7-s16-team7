from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.index, name='books'),
    path('author_id/<int:pk>/', views.all_books_author_id, name='all_books_author_id'),
    path('<int:pk>/', views.by_id, name='book'),
]