from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PageCount(models.Model):
    visits = models.IntegerField(default=0)
    page = models.URLField(default = 'defaultPage')