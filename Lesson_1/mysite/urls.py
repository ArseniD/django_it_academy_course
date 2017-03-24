from django.conf.urls import include, url
from django.contrib import admin

from base.views import say_hello, status, list_players

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^say_hello$', say_hello),
    url(r'^status$', status),
    url(r'^list_players$', list_players),
]

#http://127.0.0.1:8000/say_hello