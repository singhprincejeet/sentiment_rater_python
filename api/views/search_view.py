from django.http import JsonResponse, HttpResponse
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

from api.models import Tweet
from api.models import Word

from api.serializers import TweetSerializer


def search(request, query):

    try:
        tokens = tokenize(query.lower())
        words = get_words(tokens)
        tweets = get_tweets(words)
    except Word.DoesNotExist:
        return HttpResponse(status=404)
    except Tweet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False)


def tokenize(query):
    tokens = word_tokenize(query)
    return [token for token in tokens if token not in stopwords.words('english')]


def get_words(tokens):
    snowball_stemmer = SnowballStemmer("english")
    words = []
    for token in tokens:
        token = snowball_stemmer.stem(token)
        words.append(Word.objects.get(word=token))
    return words


def get_tweets(words):
    words.sort(key=lambda word: word.frequency, reverse=True)
    tweets_objects = [word.tweets for word in words]
    tweets_dict = {}
    # create dict for tweets based on their reputation
    for tweets_object in tweets_objects:
        tweets = tweets_object.all()
        for tweet in tweets:
            if tweet in tweets_dict:
                tweets_dict[tweet] += 1
            else:
                tweets_dict[tweet] = 1
    # then calculate the rank of tweets based on inverted document frequency
    tweets_dict = sorted(tweets_dict.items(), key=lambda x:x[1], reverse=True)
    result = [tweet[0] for tweet in tweets_dict]
    return result
