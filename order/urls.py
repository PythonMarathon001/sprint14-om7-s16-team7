from django.urls import path

from order import views


urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('not_returned/', views.not_returned_books, name='not_returned_books'),
    path('user_id/<int:pk>/', views.given_book, name='given_book'),
    path('given_book2/<int:pk>', views.given_book2, name='given_book2'),
    
]
