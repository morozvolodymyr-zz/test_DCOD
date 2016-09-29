import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view

from test_DCOD_app.models import Region


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
