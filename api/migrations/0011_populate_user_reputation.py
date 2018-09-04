import re

from django.db import migrations

from api.models import User, Tweet


def populate_users(_, __):
    username_pattern = "(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"
    regex = re.compile(username_pattern)

    for tweet in Tweet.objects.all():
        usernames = regex.findall(tweet.content)
        for username in usernames:
            try:
                user = User.objects.get(pk=username)
            except User.DoesNotExist:
                user = User(
                    id=username
                )
                user.save()
            finally:
                user.reputation+=1
                user.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_correct_tweets_sentiments")
    ]
    operations = [
        migrations.RunPython(populate_users),
    ]