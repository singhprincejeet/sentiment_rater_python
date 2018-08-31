from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from django.db import migrations
from api.models import Word


def populate_words_tweets(_, __):
    for word in Word.objects.all():
        tweets = word.tweets.all()
        word.frequency = len(tweets)
        word.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_word_frequency")
    ]
    operations = [
        migrations.RunPython(populate_words_tweets),
    ]