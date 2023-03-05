from django.urls import path
from .views import cartView

urlpatterns = [
    path('cart/', cartView.as_view(), name='Cart'),
]
