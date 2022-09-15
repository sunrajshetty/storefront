import email
from genericpath import exists
from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Cart, CartItem, Collection, Customer, Order, Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, Max, Min, Avg, Sum, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction, connection


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
    # TaggedItem.objects.get_tags_for(product, 1)
    # queryset = Product.objects.all()
    # queryset[0]
    # list(queryset)
    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # # collection.featured_product_pk = 1
    # collection.save()
   

    # collection = Collection.objects.create(name='a', featured_product_id=1)
    # collection.id
    # Collection.objects.filter(pk=11).update(featured_product=None)
    # collection = Collection(pk=11)
    # collection.delete()

    # Collection.objects.filter(id__gt=5).delete()
    # cart = Cart()
    # cart.save()

    # item1 = CartItem()
    # item1.cart = cart
    # item1.product_id = 1
    # item1.quantity = 1
    # item1.save()

    # item1 = CartItem.objects.get(pk=1)
    # item1.quantity = 2
    # item1.save()

    # cart = Cart(pk=1)
    # cart.delete()

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # queryset = Product.objects.raw('SELECT * FROM store_product')
    # queryset = Product.objects.raw('SELECT id, title FROM store_product')

    # cursor = connection.cursor()
    # cursor.execute('')
    # cursor.close()

    # with connection.cursor() as cursor:
    #     # cursor.execute()
    #     cursor.callproc('get_customers', [1, 2, 'a'])

    # return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
    # return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
    # return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'tags': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'product': product})
    return render(request, 'hello.html', {'name': 'Mosh'})
