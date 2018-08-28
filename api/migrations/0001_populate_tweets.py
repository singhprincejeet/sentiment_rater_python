import pandas

from datetime import datetime

from django.db import migrations

from api.models import Tweet


def populate_tweets(_, __):
    cols = ['sentiment','id','date','query_string','user','content']
    dataframe = pandas.read_csv('./data_processing/data/training_data.16000.csv',header=None, names=cols, encoding = "ISO-8859-1", low_memory=False)

    # removes unnecessary columns
    dataframe.drop(['date','query_string','user'],axis=1, inplace=True)

    for i in range(0, dataframe['id'].count()):
        tweet = Tweet(
            id=dataframe.loc[i, 'id'],
            content=dataframe.loc[i, 'content'],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        tweet.save()



def delete_tweets(_, __):
    Tweet.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial")
    ]
    operations = [
        migrations.RunPython(populate_tweets, delete_tweets),
    ]