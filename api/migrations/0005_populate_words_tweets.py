import pandas
from nltk import word_tokenize
from django.db import migrations

from api.models import Tweet
from api.models import Word


def populate_words_tweets(_, __):

    tweets = Tweet.objects.all()

    for tweet in tweets.all():
        tokens_from_tweet = word_tokenize(tweet.content)
        for token in tokens_from_tweet:
            word = Word.objects.get(word=token)
            word.tweets.add(tweet)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_populate_words")
    ]
    operations = [
        migrations.RunPython(populate_words_tweets),
    ]