import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from test_DCOD_app.models import Region, City


class DCODView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dcod.html', {})


@api_view(['GET'])
def get_regions(request):
    json_regions = {'regions':[]}
    regions_from_db = Region.objects.all()
    for reg in regions_from_db:
        json_regions['regions'].append(reg.region)
    return HttpResponse(json.dumps(json_regions), content_type='application/json', status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', 'POST'])
def update_region(request):
        json_data = JSONParser().parse(request)
        updated_region = json_data['updated_region']
        region = json_data['region']
        id_region = Region.objects.filter(region=region).first()
        for key in updated_region:
            City.objects.create(city=key, population=int(updated_region[key]), id_region=id_region)
        return HttpResponse('ok', status=status.HTTP_200_OK)
