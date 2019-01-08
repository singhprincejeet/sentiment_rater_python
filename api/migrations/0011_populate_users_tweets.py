import pandas

from django.db import migrations

from api.models import User, Tweet


def populate_users(_, __):
    cols = ['sentiment', 'id', 'date', 'query_string', 'user', 'content']
    dataframe = pandas.read_csv('./data_processing/data/training_data.16000.csv',header=None, names=cols, encoding = "ISO-8859-1", low_memory=False)

    # removes unnecessary columns
    dataframe.drop(['sentiment', 'date', 'query_string', 'content'],axis=1, inplace=True)

    for i in range(0, dataframe['id'].count()):
        tweet = Tweet.objects.get(pk=dataframe.loc[i, 'id'])
        if tweet:
            try:
                user = User.objects.get(pk=dataframe.loc[i, 'user'])
            except User.DoesNotExist:
                user = User(
                    id=dataframe.loc[i, 'user']
                )
                user.save()
            finally:
                tweet.user = user
                tweet.save()


def delete_users(_, __):
    User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_correct_tweets_sentiments")
    ]
    operations = [
        migrations.RunPython(populate_users, delete_users),
    ]
