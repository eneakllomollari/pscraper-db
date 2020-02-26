from django.urls import path

from .views import VehicleView, SellerView

urlpatterns = [
    path('vehicle/', VehicleView.as_view(), name='vehicle'),
    path('seller/', SellerView.as_view(), name='seller'),
]
