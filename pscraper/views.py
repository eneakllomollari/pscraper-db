from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vehicle, Seller
from .serializers import VehicleSerializer, SellerSerializer


class VehicleView(APIView):
    @staticmethod
    def get(request):
        params = request.query_params
        if len(params) == 0:
            return Response(Vehicle.objects.all().values())
        else:
            return Response(model_to_dict(Vehicle.objects.get(vin=request.query_params['vin'])))

    @staticmethod
    def post(request):
        vehicle_serializer = VehicleSerializer(data=request.data)
        vehicle_serializer.is_valid(raise_exception=True)
        # Checks the seller_id exists
        Seller.objects.get(id=vehicle_serializer.validated_data['seller_id'])
        vehicle = vehicle_serializer.save()
        return Response(vehicle.pk, status.HTTP_201_CREATED)


class SellerView(APIView):
    @staticmethod
    def get(request):
        params = request.query_params
        if len(params) == 0:
            return Response(Seller.objects.all().values())
        else:
            return Response(model_to_dict(Seller.objects.get(id=request.query_params['id'])))

    @staticmethod
    def post(request):
        serializer = SellerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        seller = serializer.save()
        return Response(seller.pk, status.HTTP_201_CREATED)
