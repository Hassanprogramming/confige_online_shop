from django.shortcuts import render
from django.views import View
from product.models import Product
from order.models import Order, OrderItem
from django.http import JsonResponse
import json
from store.utils import guestOrder
from .models import ShppingAddress
import datetime

# Create your views here.


class updateItemView(View):
    def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        print('Action:', action)
        print('productId:', productId)

        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product)
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()
        return JsonResponse('Item was added', safe=False)


class processOrderView(View):
    def processOrder(request):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order,  created = Order.objects.get_or_create(
                customer=customer, complete=False)

        else:
            customer, order = guestOrder(request, data)

        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShppingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['address'],
                state=data['shipping']['address'],
                zipcode=data['shipping']['address'],
            )
        return JsonResponse('Payment complete!', safe=False)
