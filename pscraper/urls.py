from django.urls import path
from django.views.decorators.cache import cache_page

from .views import SellerView, VehicleView

urlpatterns = [
    path('vehicle/', cache_page(1600)(VehicleView.as_view())),
    path('seller/', cache_page(1600)(SellerView.as_view())),
]
