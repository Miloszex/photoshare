from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()

class Observation(models.Model):
    subject = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subject')
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target')
