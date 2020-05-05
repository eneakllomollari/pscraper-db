import django_filters
from rest_framework import authentication, permissions, viewsets

from . import models, serializers


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
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
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
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post', 'patch']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
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
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('vin', 'price', 'seller', 'date')
