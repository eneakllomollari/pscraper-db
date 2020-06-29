from django.conf.urls import url
from rest_framework.routers import DefaultRouter

import pscraper.views.paginated_views
from .views import metric_views, model_views

router = DefaultRouter()
router.register(r'seller', model_views.SellerView)
router.register(r'cars-com-vehicle', model_views.CarsComView)
router.register(r'autotrader-vehicle', model_views.AutoTraderView)
router.register(r'history', model_views.HistoryView)
router.register(r'seller-paginate', pscraper.views.paginated_views.SellerPaginatedView)
router.register(r'vehicle-paginate', pscraper.views.paginated_views.VehiclePaginatedView)
router.register(r'history-paginate', pscraper.views.paginated_views.HistoryPaginatedView)

metric_urls = [
    url(r'^cars-com-vehicle-stats', metric_views.cars_com_vehicle_stats),
    url(r'^cars-com-makes-stats', metric_views.cars_com_makes_stats),
    url(r'^cars-com-makes', metric_views.cars_com_makes),
]

urlpatterns = [
    *router.urls,
    *metric_urls,
]
