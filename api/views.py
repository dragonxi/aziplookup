import json

from django.http import HttpResponse

from . import azure_ip


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


def lookup(request):
    if 'ip' in request.GET:
        r = azure_ip.lookup(request.GET["ip"])
    else:
        r = azure_ip.lookup('20.99.251.48')
    r = json.dumps(r)
    return HttpResponse(str(r))
