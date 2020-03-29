from rest_framework import serializers

from .models import Seller, Vehicle


class SellerSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=31)
    name = serializers.CharField(max_length=255)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)

    class Meta:
        model = Seller
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    vin = serializers.CharField(min_length=17, max_length=17)
    listing_id = serializers.CharField()
    make = serializers.CharField()
    model = serializers.CharField(allow_blank=True, allow_null=True, default=None)
    trim = serializers.CharField(allow_blank=True, allow_null=True, default=None)
    body_style = serializers.CharField(allow_blank=True, allow_null=True, default=None)
    mileage = serializers.IntegerField(allow_null=True, default=None)
    year = serializers.IntegerField(allow_null=True, default=None)
    price = serializers.FloatField(allow_null=True, default=None)
    first_date = serializers.DateField()
    last_date = serializers.DateField()
    duration = serializers.IntegerField()
    seller_id = serializers.IntegerField()

    class Meta:
        model = Vehicle
        fields = '__all__'
