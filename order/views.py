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