from nltk import word_tokenize
from django.db import migrations

from api.models import Tweet
from api.models import Word


def lowercase_words(_, __):
    for word in Word.objects.all():
        lowercased = str(word.word).lower()
        if Word.objects.filter(word=lowercased).count() > 0:
            word.delete()
        else:
            word.word = lowercased
            word.save()


def undo_lowercase_words(_, __):
    Word.objects.all().delete()

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
            frequency=-1
        )
        word.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_populate_words_tweets")
    ]
    operations = [
        migrations.RunPython(lowercase_words, undo_lowercase_words),
    ]
