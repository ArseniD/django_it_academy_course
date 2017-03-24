from django.core            import serializers
from django.shortcuts       import render
from django.template        import Template, Context
from django.http            import HttpResponse, JsonResponse
from django.utils           import version

from base.models            import Player

import json
import platform

def say_hello(request):
    msg = 'Hello, world!'
    return HttpResponse(msg)

def status(request):
    template_data = {
        "Django_version": version.get_complete_version(),
        "Python_version": platform.python_version(),
    }
    return render(request, 'status.html', template_data)



def list_players(request):
    data = Player.objects.all()
    result_list = [data.name for data in data]
    return HttpResponse(json.dumps(result_list, ensure_ascii=False)))

    # return JsonResponse( {'list_players':data} )
    # result_list = list(Player.objects.all().values('name'))
    # return HttpResponse(json.dumps(result_list))