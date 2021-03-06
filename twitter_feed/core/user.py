
class User:

    def __init__(
        self,
        name: str = None,
        id_: str = None,
        screen_name: str = None
    ):
        self.id_ = id_
        self.name = name
        self.screen_name = screen_name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def from_dict(cls, user_dict: dict):
        return cls(
            name=user_dict.get('name'),
            id_=user_dict.get('id_str'),
            screen_name=user_dict.get('screen_name')
        )
