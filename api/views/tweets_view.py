from django.http import JsonResponse

from rest_framework.parsers import JSONParser

from api.models import Tweet

from ..serializers.tweet_serializer import TweetSerializer


def tweets(request):
    if request.method == 'GET':
        tweets_list = Tweet.objects.all()[:10]
        serializer = TweetSerializer(tweets_list, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)