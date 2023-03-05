from django.urls import path
from .views import shopView
from store.views import postView

urlpatterns = [
    path('shop/', shopView.as_view(), name='Shop'),
    path('shop/<int:pid>/', postView.as_view(), name="post"),
]
