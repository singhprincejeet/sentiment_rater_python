from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from django.db import migrations

from api.models import Tweet
from api.models import Word


def populate_words_tweets(_, __):

    tweets = Tweet.objects.all()

    i = 0

    snowball_stemmer = SnowballStemmer("english")

    for tweet in tweets.all():
        tokens_from_tweet = word_tokenize(str(tweet.content).lower())
        for token in tokens_from_tweet:
            try:
                token = snowball_stemmer.stem(token)
                word = Word.objects.get(word=token)
            except Word.DoesNotExist:
                continue
            word.tweets.add(tweet)
        if i % 1000 == 0:
            print(str(i) + " tweets done")
        i += 1

def undo_populate_words_tweets(_, __):

    words = Word.objects.all()

    for word in words.all():
        word.tweets.clear()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_stem_words")
    ]
    operations = [
        migrations.RunPython(populate_words_tweets, undo_populate_words_tweets),
    ]
