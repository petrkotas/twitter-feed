import pytest
import requests

from twitter_feed.twitter.api import TwitterAPI, TwitterError


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
