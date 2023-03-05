from django.views import View
from django.shortcuts import render, get_object_or_404
from product.models import Product
from store.models import Website
from store.utils import cartData
# Create your views here.


class shopView(View):
    def get(self, request):
        data = cartData(request)
        cartItems = data['cartItems']

        lux_2 = Product.objects.filter(luxury_2=True)
        lux_1 = Product.objects.filter(luxury_1=True)
        lux = Product.objects.filter(luxury=True)
        website = Website.objects.all()
        products = Product.objects.filter(luxury=False, luxury_1=False, luxury_2=False)
        return render(request, 'shop/shop.html', {'products': products,'website': website, 'cartItems': cartItems, 'lux':lux, 'lux_1':lux_1, 'lux_2':lux_2})

