from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import metric_views, model_views

router = DefaultRouter()
router.register(r'seller', model_views.SellerView)
router.register(r'vehicle', model_views.VehicleView)
router.register(r'history', model_views.HistoryView)
router.register(r'seller-paginate', model_views.SellerPaginatedView)
router.register(r'vehicle-paginate', model_views.VehiclePaginatedView)
router.register(r'history-paginate', model_views.HistoryPaginatedView)

metric_urls = [
    url(r'^vehicle-stats', metric_views.vehicle_stats),
    url(r'^makes', metric_views.makes),
]

urlpatterns = [
    *router.urls,
    *metric_urls,
]
