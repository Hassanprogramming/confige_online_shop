from django.urls import path
from .views import checkoutView

urlpatterns = [
    path('checkout/', checkoutView.as_view(), name='Checkout'),
]
