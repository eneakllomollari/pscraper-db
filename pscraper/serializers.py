from rest_framework import serializers

from .models import Seller, Vehicle


class SellerSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True, max_length=31)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    rating = serializers.CharField(required=True)

    class Meta:
        model = Seller
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    vin = serializers.CharField(required=True, min_length=17, max_length=17)
    listing_id = serializers.CharField(required=True)
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=True)
    body_style = serializers.CharField(required=True)
    mileage = serializers.IntegerField(required=True)
    year = serializers.IntegerField(required=True)
    first_date = serializers.DateField(required=True)
    last_date = serializers.DateField(required=True)
    duration = serializers.IntegerField(required=True)
    seller_id = serializers.IntegerField(required=True)

    class Meta:
        model = Vehicle
        fields = '__all__'
