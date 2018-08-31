from django.http import JsonResponse, HttpResponse
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

from api.models import Tweet
from api.models import Word

from api.serializers import TweetSerializer


def search(request, query):

    try:
        snowball_stemmer = SnowballStemmer("english")
        tokens = word_tokenize(query)
        tokens = [token for token in tokens if token not in stopwords.words('english')]
        words = []
        tweets = []
        for token in tokens:
            token = snowball_stemmer.stem(token)
            words.append(Word.objects.get(word=token))
        for word in words:
            for tweet in word.tweets.all():
                tweets.append(tweet)
        if len(tweets) > 10:
            tweets = tweets[:10]
    except Word.DoesNotExist:
        return HttpResponse(status=404)
    except Tweet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False)