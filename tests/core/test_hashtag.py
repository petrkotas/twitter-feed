from twitter_feed.core.hashtag import Hashtag


def test_hashtag_full():
    hashtag_dict = {
        'text': 'bagr'
    }

    test_hashtag = Hashtag.from_dict(hashtag_dict)

    assert test_hashtag.text == hashtag_dict['text']