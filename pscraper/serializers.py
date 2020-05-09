from rest_framework import serializers

from . import models


class SellerSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=31)
    name = serializers.CharField(max_length=255)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)

    class Meta:
        model = models.Seller
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
    seller_id = serializers.PrimaryKeyRelatedField(source='seller', read_only=True)

    class Meta:
        model = models.Vehicle
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    vin = serializers.CharField(min_length=17, max_length=17)
    price = serializers.FloatField(allow_null=True, default=None)
    seller_id = serializers.PrimaryKeyRelatedField(source='seller', read_only=True)
    date = serializers.DateField()
    mileage = serializers.IntegerField(allow_null=True, default=None)

    class Meta:
        model = models.History
        fields = '__all__'
