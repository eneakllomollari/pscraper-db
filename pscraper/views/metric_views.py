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
def cars_com_makes_stats(_):
    all_makes = CarsComVehicle.objects.values_list('make', flat=True).distinct()
    resp = {'makes_count': all_makes.count()}
    for make in all_makes:
        resp[make] = {}
        for metric in ['price', 'duration', 'mileage', 'year']:
            resp[make][metric] = {
                'average': get(CarsComVehicle.objects.filter(make=make).aggregate(Avg(metric))),
                'standard_deviation': get(CarsComVehicle.objects.filter(make=make).aggregate(StdDev(metric))),
                'variance': get(CarsComVehicle.objects.filter(make=make).aggregate(Variance(metric))),
                'max': get(CarsComVehicle.objects.filter(make=make).aggregate(Max(metric))),
                'min': get(CarsComVehicle.objects.filter(make=make).aggregate(Min(metric))),
            }
    return Response(resp)


def get(value):
    return list(value.values())[0]
