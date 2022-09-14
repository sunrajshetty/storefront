from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q



def say_hello(request):
    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
