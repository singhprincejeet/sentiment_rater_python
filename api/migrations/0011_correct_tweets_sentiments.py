import pandas

from django.db import migrations

from api.models import Tweet, Sentiment


def populate_tweets_with_sentiments(_, __):
    cols = ['sentiment', 'id', 'date', 'query_string', 'user', 'content']
    dataframe = pandas.read_csv('./data_processing/data/training_data.16000.csv',header=None, names=cols, encoding = "ISO-8859-1", low_memory=False)

    # removes unnecessary columns
    dataframe.drop(['date', 'query_string', 'user', 'content'],axis=1, inplace=True)

    for i in range(0, dataframe['id'].count()):
        tweet = Tweet.objects.get(pk=dataframe.loc[i, 'id'])
        tweet.sentiment_id = dataframe.loc[i, 'sentiment']
        tweet.save()


def undo_populate_tweets_with_sentiments(_, __):
    tweets = Tweet.objects.all()

    for tweet in tweets:
        tweet.sentiment_id = -1
        tweet.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_add_word_frequency")
    ]
    operations = [
        migrations.RunPython(
            populate_tweets_with_sentiments,
            undo_populate_tweets_with_sentiments
        ),
    ]
