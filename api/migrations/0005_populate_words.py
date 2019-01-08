from nltk import word_tokenize
from django.db import migrations

from api.models import Tweet
from api.models import Word


def populate_words(_, __):

    tweets = Tweet.objects.all()
    all_tokens = []

    for tweet in tweets:
        tokens_from_tweet = word_tokenize(tweet.content)
        for token in tokens_from_tweet:
            if token not in all_tokens:
                all_tokens.append(token)

    for token in all_tokens:
        word = Word(
            word=token,
        )
        word.save()


def delete_words(_, __):
    Word.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_populate_tweets_with_sentiments")
    ]
    operations = [
        migrations.RunPython(populate_words, delete_words),
    ]
