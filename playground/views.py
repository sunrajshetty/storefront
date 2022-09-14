from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F



def say_hello(request):
    queryset = Product.objects.filter(inventory=F('collection_id'))

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
