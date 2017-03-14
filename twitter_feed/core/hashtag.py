class Hashtag:

    def __init__(
        self,
        text: str = None
    ):
        self.text = text

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def from_dict(cls, hashtag_dict: dict):
        return cls(
            text=hashtag_dict.get('text')
        )
