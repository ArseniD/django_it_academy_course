import datetime

from django.db              import models
from django.utils           import timezone
from django.utils.encoding  import force_bytes

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=40)
    cookie_count = models.IntegerField()
    created = models.DateField()
    #created = models.DateTimeField('date published')

    def __str__(self):
        return force_bytes('Player name: {}, '
                           'email: {}, '
                           'password: {}, '
                           'count of cookie: {}, '
                           'created: {} '.format( self.name, self.email, self.password, self.cookie_count, self.created))
         # Note use of django.utils.encoding.force_bytes() here because
         # first_name and last_name will be unicode strings.

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)


