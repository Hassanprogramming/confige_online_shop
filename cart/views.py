from django.views import View
from store.utils import cartData
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


class cartView(View):
    def get(self, request):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        return render(request, 'cart/cart.html', {'items': items, 'order': order, 'cartItems': cartItems})
