# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Money(models.Model):
    player_id = models.IntegerField()
    currency_id = models.CharField(max_length=20, blank=True, null=True)
    amount  = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    # player  = models.ForeignKey(Player)

    def __unicode__(self):
        msg = u'player_id={}, currency_id={}, amount={}'
        return msg.format(self.player_id, self.currency_id,  self.amount)

    class Meta:
        managed = False
        verbose_name_plural = 'Money'
        db_table = 'money'


class Player(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u'name={}, email={}'.format(self.name, self.email)

    class Meta:
        managed = False
        db_table = 'player'