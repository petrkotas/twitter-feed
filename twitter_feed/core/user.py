
class User:

    def __init__(
        self,
        name: str = None,
        screen_name: str = None
    ):
        self.name = name
        self.screen_name = screen_name

    @classmethod
    def from_dict(cls, user_dict: dict):
        return cls(
            name=user_dict['name'],
            screen_name=user_dict['screen_name']
        )
