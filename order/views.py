import datetime
from multiprocessing import context
from django.shortcuts import render
from .models import Book

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order/order_list.html', context)


def not_returned_books(request):
    user_info = Order.get_not_returned_books
    context = {'not_returned_books': user_info}
    return render(request, 'order/not_returned_books.html', context)

def given_book(request, pk):
    given_book = list(Order.objects.all().filter(customuser_id=pk))
    user = CustomUser.objects.filter(pk=pk)[0]
    context = {"given_book": given_book,
               "title": f"User id: {pk}",
               "id": f"{pk}",
               "user" : user,
               }
    return render(request, 'order/given_book.html', context)