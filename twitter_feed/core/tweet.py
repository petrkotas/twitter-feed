from datetime import datetime
import typing

from twitter_feed.core.user import User
from twitter_feed.core.hashtag import Hashtag


class Tweet:

    def __init__(
        self,
        id_: str = None,
        text: str = None,
        date: str = None,
        hashtags: typing.List[str] = None,
        mentions: typing.List[str] = None,
        user: User = None
    ):
        self.id_ = id_
        self.text = text
        self.date = date
        self.hashtags = hashtags
        self.mentions = mentions
        self.user = user

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def from_dict(cls, tweet_dict: dict = None):
        return cls(
            id_=tweet_dict.get('id_str'),
            text=tweet_dict.get('text'),
            date=datetime.strptime(tweet_dict.get('created_at'), '%a %b %d %X %z %Y'),
            hashtags=[Hashtag.from_dict(hsh) for hsh in tweet_dict.get('hashtags')],
            mentions=[User.from_dict(usr) for usr in tweet_dict.get('mentions')],
            user=User.from_dict(tweet_dict['user'])
        )
