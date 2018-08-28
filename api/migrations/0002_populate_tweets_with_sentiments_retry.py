import pandas

from datetime import datetime

from django.db import migrations
from api.models import Tweet


def populate_tweets(_, __):

    tweets = Tweet.objects.all()

    for tweet in tweets:
        # negative tweets after this id
        if tweet.id > 1467822272:
            tweet.sentiment_id=4
            tweet.save()


def delete_tweets(_, __):
    Tweet.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_populate_tweets_with_sentiments")
    ]
    operations = [
        migrations.RunPython(populate_tweets, delete_tweets),
    ]