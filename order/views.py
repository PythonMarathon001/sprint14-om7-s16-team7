import datetime
from django.shortcuts import render
from .models import Book

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
import pytz


def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order/order_list.html', context)


def not_returned_books(request):
<<<<<<< Updated upstream
    user_info = [order for order in Order.objects.all() if order.end_at is None]
    context = {'not_returned_books':user_info}
=======
    user_info = Order.get_not_returned_books
    context = {'not_returned_books': user_info}
>>>>>>> Stashed changes
    return render(request, 'order/not_returned_books.html', context)
