from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F



def say_hello(request):
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    # queryset = Product.objects.all()[:5]
    queryset = Product.objects.all()[5:10]

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'product': product})
