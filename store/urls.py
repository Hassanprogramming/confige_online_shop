from django.urls import path
from .views import storeView, postView, AboutView

urlpatterns = [
    path('', storeView.as_view(), name='Home'),
    path('<int:pid>/', postView.as_view(), name="post"),
    path('about us', AboutView.as_view(), name="about"),
]
