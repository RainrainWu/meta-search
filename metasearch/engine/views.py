import json

from selenium import webdriver
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import resp
from . import search


class Histories(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Histories, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        links = {"self": {"href": "/histories"}}
        message = resp.build_status(200, "resource accessed successfully.")
        histories = models.History.objects.all().order_by("created_at")
        data = [model_to_dict(x, fields=["created_at", "keyword", "result"]) for x in histories]
        for d in data:
            d["result"] = json.loads(d["result"])
        payload = resp.build_hateoas(links, message, data)
        return JsonResponse(payload, status=200, json_dumps_params={'indent': 2})

    def post(self, request, *args, **kwargs):
        links = {"self": {"href": "/histories"}}
        try:
            keyword = json.loads(request.body.decode("utf-8"))["keyword"]
        except KeyError:
            message = resp.build_status(400, "please specified searching keyword")
            payload = resp.build_hateoas(links, message)
            return JsonResponse(payload, status=400, json_dumps_params={'indent': 2})

        message = resp.build_status(201, "resource created successfully.")
        try:
            data = model_to_dict(models.History.objects.get(keyword=keyword))
        except:
            data = search.search_meta(keyword)
            history = models.History(
                keyword=keyword,
                result=json.dumps(data, indent=4)
            )
            history.save()

        payload = resp.build_hateoas(links, message, data)
        return JsonResponse(payload, status=201, json_dumps_params={'indent': 2})
