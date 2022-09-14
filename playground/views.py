import email
from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Collection, Customer, Order, Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, Max, Min, Avg, Sum, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem




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
    # result = Product.objects.filter(collection__id=3).aggregate(min_price=Min('unit_price'), avg_price=Avg('unit_price'), max_price=Max('unit_price'))
    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(new_id=F('id') + 1)
    # queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # queryset = Customer.objects.annotate(orders_count=Count('order'))
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price=discounted_price)
    # queryset = Product.objects.annotate(discounted_price=F('unit_price') * 0.8)
    # queryset = Customer.objects.annotate(last_order_id=Max('order__id'))
    # queryset = Customer.objects.annotate(order_count=Count('order')).filter(order_count__gte=5)
    # queryset = Customer.objects.annotate(total_spent=Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity')))
    # queryset = Product.objects.annotate(total_sales=Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-total_sales')[:5]
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id=1)

    # return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
    # return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
    # return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
    return render(request, 'hello.html', {'name': 'Mosh', 'tags': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'product': product})
