import json

from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import resp

class Histories(View):

    def get(self, request, *args, **kwargs):
        links = {"self": {"href": "/histories"}}
        message = resp.build_status(200, "resource accessed successfully.")
        users = models.History.objects.all().order_by("created_at")
        data = [model_to_dict(x, fields=["keyword", "created_at"]) for x in users]
        payload = resp.build_hateoas(links, message, data)
        return JsonResponse(payload, status=200, json_dumps_params={'indent': 2})