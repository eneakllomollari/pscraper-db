from django.db import models


class Seller(models.Model):
    address = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=31, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} [{self.phone_number}]'


class CarsComVehicle(models.Model):
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
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)

    def __str__(self):
        return f'Cars.com - {self.make} {self.model} [{self.vin}] [{self.listing_id}]'


class AutoTraderVehicle(models.Model):
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
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)

    def __str__(self):
        return f'AutoTrader - {self.make} {self.model} [{self.vin}] [{self.listing_id}]'


class History(models.Model):
    vin = models.CharField(max_length=17)
    price = models.FloatField(blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    date = models.DateField()
    mileage = models.IntegerField(blank=True, null=True)
    marketplace = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.vin}'

    class Meta:
        verbose_name = verbose_name_plural = 'Dynamic Data'
