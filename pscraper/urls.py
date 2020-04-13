from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'vehicle', views.VehicleView)
router.register(r'seller', views.SellerView)
router.register(r'history', views.HistoryView)

urlpatterns = [
    url(r'^', include(router.urls))
]
