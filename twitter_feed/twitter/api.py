import base64
import typing
from urllib.parse import urljoin

import requests

from twitter_feed.mock.tweets import HOME_TIMELINE, USER_TIMELINE


class TwitterError(Exception):

    def __init__(self, html_error: int, twitter_error: typing.List[dict], *args, **kwargs):
        self.html_error = html_error
        self.twitter_error = twitter_error

        super().__init__(*args, **kwargs)


class MockAPI:

    def __init__(self, *args, **kwargs):
        pass

    def get_home_timeline(self) -> typing.List[dict]:
        return HOME_TIMELINE

    def get_user_timeline(self, user: str = None) -> typing.List[dict]:
        return USER_TIMELINE

    def get_hashtag_timeline(self, hashtag: str = None) -> typing.List[dict]:
        return USER_TIMELINE

    def get_user_replies(self, user) -> typing.List[dict]:
        return USER_TIMELINE


class TwitterAPI:
    TWITTER_AUTH = 'https://api.twitter.com/oauth2/token'

    def __init__(self, api_url, api_key, api_secret):
        self.api_url = api_url
        oauth2_token = '{}:{}'.format(
            api_key, api_secret
        )

        headers = {
            'Authorization': 'Basic {}'.format(
                base64.b64encode(oauth2_token.encode('ascii')).decode('utf-8')
            ),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        body = 'grant_type=client_credentials'

        response = requests.post(self.TWITTER_AUTH, headers=headers, data=body)

        if response.status_code == 200:
            self.auth_token = response.json().get('access_token')
        else:
            parsed = response.json()
            exception = TwitterError(response.status_code, parsed)

            raise exception

    def call_api(self, method=None, params=None):
        headers = {'Authorization': 'Bearer ' + self.auth_token}

        url = urljoin(self.api_url, method)

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            parsed = response.json()
            exception = TwitterError(response.status_code, parsed)

            raise exception

    def get_home_timeline(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_user_timeline(self, user: str = None) -> typing.List[dict]:
        return self.call_api(method='statuses/user_timeline.json', params={'screen_name': user, 'count': 30})

    def get_hashtag_timeline(self, hashtag: str = None) -> typing.List[dict]:
        response = self.call_api(method='search/tweets.json', params={'q': '#{}'.format(hashtag), 'count': 30})
        return response.get('statuses')

    def get_user_replies(self, user) -> typing.List[dict]:
        response = self.call_api(method='search/tweets.json', params={'q': 'to:{}'.format(user)})
        return response.get('statuses')

