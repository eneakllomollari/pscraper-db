from django.db.models import Avg, Max, Min, StdDev, Variance
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import CarsComVehicle


@api_view()
def cars_com_vehicle_stats(request):
    vehicles = CarsComVehicle.objects.filter(**request.query_params.dict())
    resp = {'count': vehicles.count()}
    for metric in ['price', 'duration', 'mileage', 'year']:
        resp[metric] = {
            'average': get(vehicles.aggregate(Avg(metric))),
            'standard_deviation': get(vehicles.aggregate(StdDev(metric))),
            'variance': get(vehicles.aggregate(Variance(metric))),
            'max': get(vehicles.aggregate(Max(metric))),
            'min': get(vehicles.aggregate(Min(metric))),
        }
    return Response(resp)


@api_view()
def cars_com_makes(_):
    return Response(CarsComVehicle.objects.values_list('make', flat=True).distinct())


@api_view()
def cars_com_make_stats(request):
    if len(request.query_params) > 1 or 'make' not in request.query_params.dict():
        raise Exception('Only one filter allowed: `make`')
    vehicles = CarsComVehicle.objects.filter(**request.query_params.dict())
    all_makes = vehicles.values_list('make', flat=True).distinct()
    resp = {}
    for make in all_makes:
        for metric in ['price', 'duration', 'mileage', 'year']:
            resp[metric] = {
                'average': get(CarsComVehicle.objects.filter(make=make).aggregate(Avg(metric))),
                'standard_deviation': get(CarsComVehicle.objects.filter(make=make).aggregate(StdDev(metric))),
                'variance': get(CarsComVehicle.objects.filter(make=make).aggregate(Variance(metric))),
                'max': get(CarsComVehicle.objects.filter(make=make).aggregate(Max(metric))),
                'min': get(CarsComVehicle.objects.filter(make=make).aggregate(Min(metric))),
            }
    return Response(resp)


def get(value):
    return list(value.values())[0]
