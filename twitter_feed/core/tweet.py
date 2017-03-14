import typing

from twitter_feed.core.user import User


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

    @classmethod
    def from_dict(cls, tweet_dict: dict = None):
        return cls(
            id_=tweet_dict['id_str'],
            text=tweet_dict['text'],
            date=tweet_dict['created_at'],
            hashtags=tweet_dict['hashtags'],
            mentions=tweet_dict['mentions'],
            user=User.from_dict(tweet_dict['user'])
        )
