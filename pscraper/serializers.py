from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.History
        fields = '__all__'


class CarsComVehicleSerializer(serializers.ModelSerializer):
    vin = serializers.CharField(min_length=17, max_length=17,
                                validators=[UniqueValidator(models.CarsComVehicle.objects.all())])

    class Meta:
        model = models.CarsComVehicle
        fields = '__all__'


class AutoTraderVehicleSerializer(serializers.ModelSerializer):
    vin = serializers.CharField(min_length=17, max_length=17,
                                validators=[UniqueValidator(models.AutoTraderVehicle.objects.all())])

    class Meta:
        model = models.AutoTraderVehicle
        fields = '__all__'
