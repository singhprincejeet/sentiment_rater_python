from django.db import migrations
from api.models import Sentiment


def populate_sentiments(_, __):
    positive = Sentiment(
        id=0,
        value="positive"
    )
    positive.save()
    negative = Sentiment(
        id=4,
        value="negative"
    )
    negative.save()


def delete_sentiments(_, __):
    Sentiment.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_populate_tweets")
    ]
    operations = [
        migrations.RunPython(populate_sentiments, delete_sentiments),
    ]