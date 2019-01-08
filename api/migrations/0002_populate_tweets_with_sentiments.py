from django.db import migrations
from api.models import Tweet, Sentiment


def populate_tweets(_, __):

    tweets = Tweet.objects.all()

    for tweet in tweets:
        # negative tweets after this id
        if tweet.id > 1467822272:
            tweet.sentiment=Sentiment.objects.get(id=4)
            tweet.save()
        else:
            tweet.sentiment=Sentiment.objects.get(id=0)
            tweet.save()


def delete_tweets(_, __):
    tweets = Tweet.objects.all()

    for tweet in tweets:
        tweet.sentiment=Sentiment.objects.get(id=0)
        tweet.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_populate_sentiments")
    ]
    operations = [
        migrations.RunPython(populate_tweets, delete_tweets),
    ]
