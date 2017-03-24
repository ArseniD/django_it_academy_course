from base.models import Player#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



    # Player.objects.filter(email__contains='by')
    # Money.objects.exclude(currency_id=None).values_list('currency_id',flat = True).distinct()
    # Money.objects.order_by('currency_id').aggregate(Avg('amount'))
    # Money.objects.values('currency_id').annotate(total=Sum('amount'))






    # Rating.objects.filter(
    # attribute__in=attributes).annotate(
    # acount=Count('location')).aggregate(Sum('score'))

    # Money.objects.filter(currency_id__in=currency_id) \
    # .values('currency_id') \
    # .annotate(score = Sum('amount')) \
    # .order_by('-currency_id')