from __future__ import unicode_literals

from django.db import models
import datetime
from PIL import Image

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

    def postprocess(self):
        i = Image.open(self.image.path)
        (width, height) = i.size
        print width, height
        if width > height:
            i.rotate(90)
            i.save(self.image.path, "JPEG")
            i = Image.open(self.image.path)
            (width, height) = i.size
            print "rotated"
        print width, height
        ratio = float(width)/float(height)
        print ratio
        max_height = int(1920 / 2)
        if height > max_height:
            new_height = max_height
            new_width = int(ratio*new_height)
            new_size = (new_width, new_height)
            i.thumbnail(new_size, Image.ANTIALIAS)
        i.save(self.image.path, "JPEG")
        
