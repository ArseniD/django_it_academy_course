from django.shortcuts   import render
from django.db.models   import Avg
from django.http        import HttpResponse, JsonResponse
from django.template    import Template, Context
from django.utils       import version
from django.core        import serializers

from datetime           import datetime
from models             import Player,Money

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


def players_list(request):
    data = Player.objects.all()
    result_list = [data.name for data in data]
    return HttpResponse(json.dumps(result_list, ensure_ascii=False))
    # return JsonResponse( {'list_players':data} )
    # result_list = list(Player.objects.all().values('name'))


def verbose_player_info(request, player_id):
    return HttpResponse("Hello, user with id `{}`".format(player_id))


def player_money(request, id=None):
    template_data = {
        "player_id": Money.objects.filter(player_id=id)
        # "player_id2": Money.objects.filter(player_id=id).filter(currency_id__icontains='dead_crystals')
    }

    # data = Money.objects.all().filter(player_id=id)
    # result_list = [data.currency_id for data in data]
    return render(request, 'player_money.html', template_data)


def django_info(request):
    template_data = {
        "first_name": "Django",
        "last_name": "Unchained",
        "version": "1.0",
        "created": datetime.now()
    }
    return render(request, 'django_info.html', template_data)


def players_table(request):
    template_data = {
        "player_list": Player.objects.all(),
        "version": "1.0"
    }
    return render(request, 'players_table.html', template_data)


# def player_name(request, name=None)
#
#     if 'q' in request.GET:
#         q = request.GET['q']
#         if not q:
#             error = True
#         else:
#             books = Book.objects.filter(title__icontains=q)
#             return render(request, 'search_results.html',
#                 {'books': books, 'query': q})
#
#     template_data = {
#         "player_name": Player.objects.filter(name__icontains=q),
#         "player_money": Money.objects.all()
#     }
#     return render(request, 'players_table.html', template_data)


def player_name(request):
    query = Money.objects.filter(player_id__name=request.GET['name'])
    data = serializers.serialize('json', qset)
    return HttpResponse(data)