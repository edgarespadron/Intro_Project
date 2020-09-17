from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app_1'
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
