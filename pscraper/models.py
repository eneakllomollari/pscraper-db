from django.db import models


class Seller(models.Model):
    phone_number = models.CharField(unique=True, max_length=31)
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f'{self.name} [{self.phone_number}]'


class Vehicle(models.Model):
    vin = models.CharField(primary_key=True, unique=True, max_length=17)
    listing_id = models.CharField(unique=True, max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    trim = models.CharField(max_length=255)
    body_style = models.CharField(max_length=255)
    mileage = models.IntegerField()
    year = models.IntegerField()
    first_date = models.DateField()
    last_date = models.DateField()
    duration = models.IntegerField()
    seller_id = models.IntegerField()

    def __str__(self):
        return f'{self.make} {self.model} [{self.vin}]'
