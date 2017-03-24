#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



########################################################################################################################

    # django-admin startproject mysite
    # python manage.py startapp base
    # python manage.py syncdb
    # python manage.py makemigrations base
    # python manage.py sqlmigrate base 001
    # python manage.py migrate
    # python manage.py shell

    # from base.models import Player
    # Player.objects.all()
    # p = Player()
    # p.name = 'vasya'
    # p.email = 'vasya@tut.by'
    # p.cookie_count = 4
    # p.password ='123'
    # import datetime
    # p.created=datetime.datetime.now()
    # p.save()

    # python manage.py shell
    # >>> from base.models import Player
    # Player.objects.all()
    # [<Player: name: vasya, email: vasya@tut.by, password: 123, count of cookie:  4, created: 2016-01-20>]
    # Player.objects.filter(id=1)
    # [<Player: name: vasya, email: vasya@tut.by, password: 123, count of cookie:  4, created: 2016-01-20>]

    # Player.objects.filter(name__startswith='v')
    # [<Player: name: vasya, email: vasya@tut.by, password: 123, count of cookie:  4, created: 2016-01-20>]

    # from django.utils import timezone
    # current_year = timezone.now().year
    # Player.objects.get(created__year=current_year)
    # <Player: name: vasya, email: vasya@tut.by, password: 123, count of cookie:  4, created: 2016-01-20>

    # >>> Player.objects.get(id=2)
    # DoesNotExist: Player matching query does not exist.

    # Make sure our custom method worked.
    # >>> q = Player.objects.get(pk=1)
    # >>> q.was_published_recently()
    # True



