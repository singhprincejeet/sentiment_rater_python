import pandas
from nltk import word_tokenize
from django.db import migrations

from api.models import Tweet
from api.models import Word


def populate_words_tweets(_, __):

    tweets = Tweet.objects.all()

    i = 0

    for tweet in tweets.all():
        tokens_from_tweet = word_tokenize(str(tweet.content).lower())
        for token in tokens_from_tweet:
            try:
                word = Word.objects.get(word=token)
            except Word.DoesNotExist:
                continue
            word.tweets.add(tweet)
        if i % 1000 == 0:
            print(str(i) + " tweets done")
        i += 1


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_auto_20180821_0843")
    ]
    operations = [
        migrations.RunPython(populate_words_tweets),
    ]