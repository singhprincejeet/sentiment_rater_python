import pandas

from django.db import migrations

from api.models import Tweet


def populate_users(_, __):
    cols = ['sentiment', 'id', 'date', 'query_string', 'user', 'content']
    dataframe = pandas.read_csv('./data_processing/data/training_data.16000.csv',header=None, names=cols, encoding = "ISO-8859-1", low_memory=False)

    # removes unnecessary columns
    dataframe.drop(['date', 'query_string', 'user', 'content'],axis=1, inplace=True)

    for i in range(0, dataframe['id'].count()):
        tweet = Tweet.objects.get(pk=dataframe.loc[i, 'id'])
        tweet.sentiment_id = dataframe.loc[i, 'sentiment']
        tweet.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_populate_users_tweets")
    ]
    operations = [
        migrations.RunPython(populate_users),
    ]