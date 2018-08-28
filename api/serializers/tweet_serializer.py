from rest_framework import serializers

from api.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    sentiment = serializers.SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'updated_at', 'created_at', 'sentiment')