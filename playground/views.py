from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist




def say_hello(request):
    query_set = Product.objects.filter(description__isnull=True)

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
