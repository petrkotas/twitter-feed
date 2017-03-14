from twitter_feed.core.user import User


def test_user_incomplete():
    user_dict = {
        'name': 'OAuth Dancer',
        'id_str': '119476949',
    }

    test_usr = User.from_dict(user_dict)

    assert test_usr.id_ == user_dict['id_str']
    assert test_usr.name == user_dict['name']
    assert test_usr.screen_name is None


def test_user_full():
    user_dict = {
        'name': 'OAuth Dancer',
        'screen_name': 'oauth_dancer',
        'id_str': '119476949',
    }

    test_usr = User.from_dict(user_dict)

    assert test_usr.id_ == user_dict['id_str']
    assert test_usr.name == user_dict['name']
    assert test_usr.screen_name == user_dict['screen_name']
