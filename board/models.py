from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)
    add_date = models.DateField(default=now())

    class Meta:
        ordering = ['-add_date']
