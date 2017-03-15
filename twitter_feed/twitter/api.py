import typing

import requests

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

    def get_home_timeline(self) -> typing.List[dict]:
        return []

    def get_user_timeline(self, user: str = None) -> typing.List[dict]:
        return []

    def get_hashtag_timeline(self, hashtag: str = None) -> typing.List[dict]:
        return []

