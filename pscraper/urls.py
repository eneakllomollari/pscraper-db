from django.urls import path

from .views import VehicleView, SellerView

urlpatterns = [
    path('vehicle/', VehicleView.as_view()),
    path('seller/', SellerView.as_view())
]
