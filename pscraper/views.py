from rest_framework import permissions, viewsets

from . import models, pagination, serializers


class SellerView(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing sellers.

    create:
    Create a new seller instance.

    read:
    Return an existing seller instance.
    """
    lookup_field = 'phone_number'
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post']
    filterset_fields = ('phone_number', 'address', 'name',)

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)


class VehicleView(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing vehicle instances.

    create:
    Create a new vehicle instance.

    read:
    Return an existing vehicle instance.

    partial_update:
    Update an existing vehicle instance.
    """
    lookup_field = 'vin'
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ('vin', 'listing_id', 'make', 'model', 'trim', 'body_style', 'mileage', 'year',
                        'year', 'price', 'first_date', 'last_date', 'duration', 'seller',)

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)


class HistoryView(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing history records.

    create:
    Create a new history record instance.

    read:
    Return an existing history records.
    """
    lookup_field = 'vin'
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post']
    filterset_fields = ('vin', 'price', 'seller', 'date')


class SellerPaginatedView(SellerView):
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.StandardResultsSetPagination


class VehiclePaginatedView(VehicleView):
    http_method_names = ['get']
    pagination_class = pagination.StandardResultsSetPagination


class HistoryPaginatedView(HistoryView):
    http_method_names = ['get']
    pagination_class = pagination.StandardResultsSetPagination
