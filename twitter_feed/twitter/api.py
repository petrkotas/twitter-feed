import typing
from urllib.parse import urljoin

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from twitter_feed.mock.tweets import HOME_TIMELINE, USER_TIMELINE


class TwitterError(Exception):

    def __init__(self, html_error, html_status, twitter_error, twitter_status, *args, **kwargs):
        self.html_status = html_error
        self.html_error = html_error
        self.twitter_error = twitter_error
        self.twitter_status = twitter_status

        super().__init__(*args, **kwargs)


class MockAPI:

    def get_home_timeline(self) -> typing.List[dict]:
        return HOME_TIMELINE

    def get_user_timeline(self, user: str = None) -> typing.List[dict]:
        return USER_TIMELINE

    def get_hashtag_timeline(self, hashtag: str = None) -> typing.List[dict]:
        return USER_TIMELINE


class TwitterAPI:

    def __init__(self, api_url, api_key, api_secret):
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret

        client = BackendApplicationClient(client_id=self.api_key)
        oauth = OAuth2Session(client=client)

        self.auth_token = oauth.fetch_token(token_url=self.api_url, client_id=self.api_key, client_secret=self.api_secret)

    def call_api(self, method=None, params=None):
        headers = {'Authorization': 'Bearer ' + self.auth_token}

        url = urljoin(self.api_url, method)

        response = requests.get(url, headers=headers, params=params)

        return response

    def get_home_timeline(self) -> typing.List[dict]:
        return []

    def get_user_timeline(self, user: str = None) -> typing.List[dict]:
        return self.call_api(method='statuses/user_timeline.json', params={'screen_name': user, 'count': 30})

    def get_hashtag_timeline(self, hashtag: str = None) -> typing.List[dict]:
        return []

