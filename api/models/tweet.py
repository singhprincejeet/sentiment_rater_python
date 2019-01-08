from django.db import models

from api.models.user import User
from api.models.sentiment import Sentiment

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)
    sentiment = models.ForeignKey(Sentiment, on_delete=models.PROTECT, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label='api'
        ordering=('created_at',)
