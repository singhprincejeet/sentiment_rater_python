from django.db import models

from api.models.sentiment import Sentiment


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    sentiment = models.ForeignKey(Sentiment, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label='api'
        ordering=('created_at',)
