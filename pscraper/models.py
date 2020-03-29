from django.db import models
from field_history.tracker import FieldHistoryTracker


class Seller(models.Model):
    address = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=31)
    name = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} [{self.phone_number}]'


class Vehicle(models.Model):
    vin = models.CharField(unique=True, max_length=17)
    listing_id = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(blank=True, null=True, max_length=255)
    trim = models.CharField(blank=True, null=True, max_length=255)
    body_style = models.CharField(blank=True, null=True, max_length=255)
    mileage = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    first_date = models.DateField()
    last_date = models.DateField()
    duration = models.IntegerField()
    seller_id = models.IntegerField()

    field_history = FieldHistoryTracker(['price'])

    def __str__(self):
        return f'{self.make} {self.model} [{self.vin}] [{self.listing_id}]'
