from django.db import models


class Sentiment(models.Model):
    value = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label='api'
        ordering=('created_at',)

    def __unicode__(self):
        return str(self.value)
