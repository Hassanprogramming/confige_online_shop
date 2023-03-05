from django.urls import path
from .views import updateItemView, processOrderView

urlpatterns = [
    path('update_item/', updateItemView.as_view(), name='update_item'),
    path('process_order/', processOrderView.as_view(), name="process_order"),
]
