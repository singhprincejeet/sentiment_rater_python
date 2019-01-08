import re

from django.db import migrations

from api.models import User, Tweet


def populate_user_reputation(_, __):
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


def undo_populate_user_reputation(_, __):
    for user in User.objects.all():
        user.reputation = -1
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_populate_users_tweets")
    ]
    operations = [
        migrations.RunPython(populate_user_reputation, undo_populate_user_reputation),
    ]
