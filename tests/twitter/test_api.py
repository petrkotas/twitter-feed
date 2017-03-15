import pytest
import requests

from twitter_feed.core.tweet import Tweet
from twitter_feed.twitter.api import TwitterAPI, TwitterError
from twitter_feed.mock.tweets import USER_TIMELINE


def test_api_auth_fail(monkeypatch):
    def fake_post(*args, **kwargs):
        class Response:
            status_code = 403

            def json(self):
                return {
                    'errors': [
                        {
                            'code': 99,
                            'message': 'Unable to verify your credentials.'
                        }
                    ]
                }
        return Response()

    # replace requests post with my fake post
    monkeypatch.setattr(requests, 'post', fake_post)

    with pytest.raises(TwitterError) as excinfo:
        api = TwitterAPI('url', 'test', 'fail')

    assert excinfo.value.twitter_error == {
        'errors': [
            {
                'code': 99,
                'message': 'Unable to verify your credentials.'
            }
        ]
    }


def test_api_auth_ok(monkeypatch):
    def fake_post(*args, **kwargs):
        class Response:
            status_code = 200

            def json(self):
                return {
                    'access_token': 'blabla'
                }
        return Response()

        # replace requests post with my fake post
        monkeypatch.setattr(requests, 'post', fake_post)

        api = TwitterAPI('url', 'test', 'fail')

        assert api.auth_token == 'blabla'


def test_api_get_user_timeline_ok(monkeypatch):
    def fake_get(*args, **kwargs):
        class Response:
            status_code = 200

            def json(self):
                return USER_TIMELINE
        return Response()

        # replace requests post with my fake post
        monkeypatch.setattr(requests, 'get', fake_get)

        api = TwitterAPI('url', 'test', 'test')
        tweets = api.get_user_timeline('test')

        assert len(tweets) == len(USER_TIMELINE)
        for tweet, tweet_dict in zip(tweets, USER_TIMELINE):
            assert tweet == Tweet.from_dict(tweet_dict)