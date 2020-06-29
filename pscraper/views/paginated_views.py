from rest_framework.pagination import LimitOffsetPagination

from .model_views import AutoTraderView, CarsComView, HistoryView, SellerView


class StandardResultsSetPagination(LimitOffsetPagination):
    default_limit = 100


class SellerPaginatedView(SellerView):
    http_method_names = ['get']
    pagination_class = StandardResultsSetPagination


class VehiclePaginatedView(CarsComView, AutoTraderView):
    http_method_names = ['get']
    pagination_class = StandardResultsSetPagination


class HistoryPaginatedView(HistoryView):
    http_method_names = ['get']
    pagination_class = StandardResultsSetPagination
