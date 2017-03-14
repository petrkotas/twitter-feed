from flask import Blueprint, jsonify, request

from twitter_feed.core.serializers.tweet_serializer import tweets_to_atom
from twitter_feed.core.tweet import Tweet
from twitter_feed.twitter.api import MockAPI


rest_view = Blueprint('rest_view', __name__, url_prefix='/rest')


@rest_view.route('/', methods=['GET'])
def home_timeline():
    api = MockAPI()

    tweets = Tweet.tweets_from_list(api.get_home_timeline())
    feed = tweets_to_atom(tweets, 'Home feed', request.url, request.host_url)

    return feed.get_response()


@rest_view.route('/users/<user:string>', methods=['GET'])
def user_timeline(user):
    api = MockAPI()

    tweets = Tweet.tweets_from_list(api.get_user_timeline(user))
    feed = tweets_to_atom(tweets, 'Feed for ' + user, request.url, request.host_url)

    return feed.get_response()

