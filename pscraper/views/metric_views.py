from django.db.models import Avg, Max, Min, StdDev, Variance
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pscraper.misc import get
from pscraper.models import Vehicle


@api_view()
def vehicle_stats(request):
    vehicles = Vehicle.objects.filter(**request.query_params.dict())
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
def makes(_):
    return Response(Vehicle.objects.values_list('make', flat=True).distinct())
