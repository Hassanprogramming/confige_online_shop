from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from store.utils import cartData
# Create your views here.


class checkoutView(View):
    def get(self, request):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        return render(request, 'checkout/checkout.html', {'cartItems':cartItems, 'items': items, 'order': order,})

