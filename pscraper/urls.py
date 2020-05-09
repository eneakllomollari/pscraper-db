from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'seller', views.SellerView)
router.register(r'vehicle', views.VehicleView)
router.register(r'history', views.HistoryView)
router.register(r'seller-paginate', views.SellerPaginatedView)
router.register(r'vehicle-paginate', views.VehiclePaginatedView)
router.register(r'history-paginate', views.HistoryPaginatedView)

urlpatterns = [
    url(r'^', include(router.urls))
]
