from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from django.db import migrations

from api.models import Tweet
from api.models import Word


def stem_words(_, __):
    snowball_stemmer = SnowballStemmer("english")

    for word in Word.objects.all():
        stemmed = snowball_stemmer.stem(word.word)
        if Word.objects.filter(word=stemmed).count() > 0:
            word.delete()
        else:
            word.word = stemmed
            word.save()


def undo_stem_words(_, __):
    Word.objects.all().delete()

    tweets = Tweet.objects.all()
    all_tokens = []

    for tweet in tweets:
        tokens_from_tweet = word_tokenize(str(tweet.content).lower())
        for token in tokens_from_tweet:
            if token not in all_tokens:
                all_tokens.append(token)

    for token in all_tokens:
        word = Word(
            word=token,
            frequency=-1,
        )
        if Word.objects.filter(word=token).count() is 0:
            word.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_populate_words_tweets_redo_after_lowercasing")
    ]
    operations = [
        migrations.RunPython(stem_words, undo_stem_words),
    ]
