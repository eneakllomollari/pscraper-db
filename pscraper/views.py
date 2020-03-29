from django.forms.models import model_to_dict
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Seller, Vehicle
from .serializers import SellerSerializer, VehicleSerializer


class VehicleView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    def get(request):
        return Response(Vehicle.objects.filter(**request.data.dict()).values())

    @staticmethod
    def post(request):
        vehicle_serializer = VehicleSerializer(data=request.data)
        vehicle_serializer.is_valid(raise_exception=True)
        return Response(model_to_dict(vehicle_serializer.save()), status.HTTP_201_CREATED)

    @staticmethod
    def patch(request):
        vehicle = Vehicle.objects.get(id=request.data['id'])
        vehicle_serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        vehicle_serializer.is_valid(raise_exception=True)
        return Response(model_to_dict(vehicle_serializer.save()))


class SellerView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    def get(request):
        return Response(Seller.objects.filter(**request.data.dict()).values())

    @staticmethod
    def post(request):
        seller_serializer = SellerSerializer(data=request.data)
        seller_serializer.is_valid(raise_exception=True)
        return Response(model_to_dict(seller_serializer.save()), status.HTTP_201_CREATED)

    @staticmethod
    def patch(request):
        seller_serializer = SellerSerializer(data=request.data, partial=True)
        seller_serializer.is_valid(raise_exception=True)
        return Response(model_to_dict(seller_serializer.save()))
