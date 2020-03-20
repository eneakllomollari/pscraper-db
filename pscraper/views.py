from django.forms.models import model_to_dict
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vehicle, Seller
from .serializers import VehicleSerializer, SellerSerializer


class VehicleView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    def get(request):
        params = request.query_params.dict()
        return Response(Vehicle.objects.filter(**params).values())

    @staticmethod
    def put(request):
        vehicle_serializer = VehicleSerializer(data=request.data)
        vehicle_serializer.is_valid(raise_exception=True)
        Seller.objects.get(id=vehicle_serializer.validated_data['seller_id'])
        instance = vehicle_serializer.save()
        return Response(model_to_dict(instance), status.HTTP_201_CREATED)

    @staticmethod
    def patch(request):
        pk = request.query_params['id']
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle_serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        vehicle_serializer.is_valid(raise_exception=True)
        vehicle_serializer.save()
        return Response(vehicle_serializer.validated_data)


class SellerView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    def get(request):
        params = request.query_params.dict()
        return Response(Seller.objects.filter(**params).values())

    @staticmethod
    def put(request):
        seller_serializer = SellerSerializer(data=request.data)
        seller_serializer.is_valid(raise_exception=True)
        instance = seller_serializer.save()
        return Response(model_to_dict(instance), status.HTTP_201_CREATED)

    @staticmethod
    def patch(request):
        pk = request.query_params['id']
        seller = Seller.objects.get(pk=pk)
        seller_serializer = SellerSerializer(seller, data=request.data, partial=True)
        seller_serializer.is_valid(raise_exception=True)
        seller_serializer.save()
        return Response(seller_serializer.validated_data)
