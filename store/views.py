from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from .models import Website, About
from .utils import cartData
# Create your views here.


class storeView(View):
    def get(self, request):
        data = cartData(request)
        cartItems = data['cartItems']

        website = Website.objects.all()
        products = Product.objects.filter(luxury=False, luxury_1=False, luxury_2=False)
        second_product = Product.objects.filter(luxury=True)
        return render(request, 'store/store.html', {'products': products, 'second_product': second_product, 'website': website, 'cartItems':cartItems})

class postView(View):
    def get(self, request, pid):
        data = cartData(request)
        cartItems = data['cartItems']
        product = get_object_or_404(Product,pk=pid)
        return render(request, 'product/product.html', {'cartItems':cartItems, 'product':product})
    
class AboutView(View):
    def get(self, request):
        about = About.objects.all()
        return render(request, 'store/about.html', {'about':about})
