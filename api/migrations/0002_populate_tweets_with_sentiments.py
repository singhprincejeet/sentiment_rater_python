import pandas

from django.db import migrations
from api.models import Tweet


def populate_tweets(_, __):
    cols = ['sentiment','id','date','query_string','user','content']
    dataframe = pandas.read_csv('./data_processing/data/training_data.16000.csv',header=None, names=cols, encoding = "ISO-8859-1", low_memory=False)

    # removes unnecessary columns
    dataframe.drop(['content','date','query_string','user'],axis=1, inplace=True)

    tweets = Tweet.objects.all()

    for tweet in tweets:
        tweet.sentiment_id=dataframe.loc[dataframe['id'] == tweet.id, 'sentiment']
        tweet.save()


def delete_tweets(_, __):
    Tweet.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_tweet_sentiment")
    ]
    operations = [
        migrations.RunPython(populate_tweets, delete_tweets),
    ]