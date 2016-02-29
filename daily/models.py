from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Quote(models.Model):
    text = models.TextField()
    image = models.FileField(upload_to='static/images/%Y/%m/%d/')
    date = models.DateField(default=datetime.date.today)

    @classmethod
    def imageForToday(self):
        # checks whether an image has been uploaded today
        today = datetime.date.today()
        try:
            entry = Quote.objects.get(date=today)
            return True
        except:
            return False
