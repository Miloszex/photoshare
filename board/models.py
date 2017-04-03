from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    description = models.TextField()
    likes = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)

