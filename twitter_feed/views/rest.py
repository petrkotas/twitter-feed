from flask import Blueprint, jsonify, request

from twitter_feed.core.serializers.tweet_serializer import tweets_to_atom
from twitter_feed.core.tweet import Tweet
from twitter_feed.twitter.api import TwitterError, TwitterAPI


rest_view = Blueprint('rest_view', __name__, url_prefix='/rest')
rest_view.api = TwitterAPI


@rest_view.record
def record_params(setup_state):
    app = setup_state.app
    if app.config['API'] == 'mock':
        from twitter_feed.twitter.api import MockAPI
        rest_view.api = MockAPI


@rest_view.route('/', methods=['GET'])
def home_timeline():
    api = rest_view.api()

    try:
        tweets = Tweet.tweets_from_list(api.get_home_timeline())
    except TwitterError as error:
        message = {
            'status': error.html_error,
            'message': error.html_status + ', ' + str(error.twitter_error) + ': ' + error.twitter_status
        }
        response = jsonify(message)
        response.status_code = error.html_error

        return response

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
    api = rest_view.api()

    try:
        tweets = Tweet.tweets_from_list(api.get_user_timeline(user))
    except TwitterError as error:
        message = {
            'status': error.html_error,
            'message': error.html_status + ', ' + str(error.twitter_error) + ': ' + error.twitter_status
        }
        response = jsonify(message)
        response.status_code = error.html_error

        return response

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


@rest_view.route('/hashtags/<string:hashtag>', methods=['GET'])
def hashtag_timeline(hashtag):
    api = rest_view.api()

    try:
        tweets = Tweet.tweets_from_list(api.get_hashtag_timeline(hashtag))
    except TwitterError as error:
        message = {
            'status': error.html_error,
            'message': error.html_status + ', ' + str(error.twitter_error) + ': ' + error.twitter_status
        }
        response = jsonify(message)
        response.status_code = error.html_error

        return response

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
