import typing



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
