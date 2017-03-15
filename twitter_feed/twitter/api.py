import typing

from twitter_feed.mock.tweets import HOME_TIMELINE, USER_TIMELINE


class MockAPI:

    def get_home_timeline(self) -> typing.List[dict]:
        return HOME_TIMELINE

    def get_user_timeline(self, user: str = None) -> typing.List[dict]:
        return USER_TIMELINE

    def get_hashtag_timeline(self, hashtag: str = None) -> typing.List[dict]:
        return USER_TIMELINE
