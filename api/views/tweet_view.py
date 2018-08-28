from django.http import JsonResponse, HttpResponse

from rest_framework.parsers import JSONParser

from api.models import Tweet

from ..serializers.tweet_serializer import TweetSerializer


def tweet(request, pk):

    try:
        tweet = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TweetSerializer(tweet)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tweet.delete()
        return HttpResponse(status=204)