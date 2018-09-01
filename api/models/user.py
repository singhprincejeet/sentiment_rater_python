from django.db import models


class User(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    reputation = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label='api'
        ordering=('created_at',)
