from django.urls import path

from order import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('not_returned/', views.not_returned_books, name='not_returned_books'),
    path('customuser_id/<int:pk>/', views.given_book, name='given_book'),
    
]
