from django.db import migrations
from api.models import Word


def add_word_frequency(_, __):
    for word in Word.objects.all():
        tweets = word.tweets.all()
        word.frequency = len(tweets)
        word.save()


def remove_word_frequency(_, __):
    for word in Word.objects.all():
        tweets = word.tweets.all()
        word.frequency = -1
        word.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_populate_words_tweets_redo_after_stemming")
    ]
    operations = [
        migrations.RunPython(add_word_frequency, remove_word_frequency),
    ]
