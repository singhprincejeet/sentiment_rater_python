from django.db import migrations

from api.models import Word


def remove_duplicate_words(_, __):

    for row in Word.objects.all():
        if Word.objects.filter(word=row.word).count() > 1:
            row.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_lowercase_words")
    ]
    operations = [
        migrations.RunPython(remove_duplicate_words),
    ]