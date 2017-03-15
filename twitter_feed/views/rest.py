from flask import Blueprint, jsonify, request

from twitter_feed.core.serializers.tweet_serializer import tweets_to_atom
from twitter_feed.core.tweet import Tweet
from twitter_feed.twitter.api import MockAPI


API = MockAPI
rest_view = Blueprint('rest_view', __name__, url_prefix='/rest')


@rest_view.route('/', methods=['GET'])
def home_timeline():
    api = API()

    tweets = Tweet.tweets_from_list(api.get_home_timeline())

    try:
        feed = tweets_to_atom(tweets, 'Home feed', request.url, request.host_url)
        response = feed.get_response()
    except Exception as error:
        message = {
            'status': 500,
            'message': str(error)
        }
        response = jsonify(message)
        response.status_code = 500

    return response


@rest_view.route('/users/<string:user>', methods=['GET'])
def user_timeline(user):
    api = API()

    tweets = Tweet.tweets_from_list(api.get_user_timeline(user))

    try:
        feed = tweets_to_atom(tweets, 'Feed for ' + user, request.url, request.host_url)
        response = feed.get_response()
    except Exception as error:
        message = {
            'status': 500,
            'message': str(error)
        }
        response = jsonify(message)
        response.status_code = 500

    return response


@rest_view.route('/hashtag/<string:hashtag>', methods=['GET'])
def hashtag_timeline(hashtag):
    api = API()

    tweets = Tweet.tweets_from_list(api.get_hashtag_timeline(hashtag))

    try:
        feed = tweets_to_atom(tweets, 'Feed for ' + hashtag, request.url, request.host_url)
        response = feed.get_response()
    except Exception as error:
        message = {
            'status': 500,
            'message': str(error)
        }
        response = jsonify(message)
        response.status_code = 500

    return response
