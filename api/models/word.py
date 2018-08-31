from django.db import models

from .tweet import Tweet


class Word(models.Model):
    word = models.CharField(max_length=140, unique=True)
    frequency = models.IntegerField()
    tweets = models.ManyToManyField(Tweet)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label='api'
        ordering=('created_at',)
