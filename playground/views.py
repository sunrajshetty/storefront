import email
from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Collection, Customer, Order, Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum




def say_hello(request):
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    # queryset = Product.objects.all()[:5]
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values('id', 'title')
    # queryset = Product.objects.values('id', 'title', 'collection__title')
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')
    # queryset = OrderItem.objects.values('product_id').distinct()
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.only('id', 'title')
    # queryset = Product.objects.defer('description')
    # queryset = Product.objects.all()
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.select_related('collection__someOtherField').all()
    # queryset = Product.objects.prefetch_related('promotions').all()
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    result = Product.objects.filter(collection__id=3).aggregate(min_price=Min('unit_price'), avg_price=Avg('unit_price'), max_price=Max('unit_price'))

    # return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
    # return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
    # return render(request, 'hello.html', {'name': 'Mosh', 'product': product})
