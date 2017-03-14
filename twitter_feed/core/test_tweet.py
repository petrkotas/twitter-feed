from twitter_feed.core.tweet import Tweet
from twitter_feed.core.user import User


def test_tweet_full():
    tweet_dict = {
        'created_at': 'Tue Aug 28 21:16:23 +0000 2012',
        'id_str': '240558470661799936',
        'text': 'just another test',
        'user': {
            'name': 'OAuth Dancer',
            'screen_name': 'oauth_dancer',
            'id_str': '119476949',
        },
        'mentions': [
            {
                'name': 'Cal',
                'id_str': '17445752',
                'screen_name': 'Cal'
            }
        ],
        'hashtags': [
            {
                'text': 'twitter'
            }
        ]
    }

    test_tweet = Tweet.from_dict(tweet_dict)

    assert test_tweet.id_ == tweet_dict['id_str']
    assert test_tweet.text == tweet_dict['text']
    assert test_tweet.user == User.from_dict(tweet_dict['user'])

    assert len(test_tweet.mentions) == len(tweet_dict['mentions'])
    for user_mention, mention in zip(test_tweet.mentions, tweet_dict['mentions']):
        assert user_mention == User.from_dict(mention)

    assert test_tweet.mentions == tweet_dict['mentions']
    assert test_tweet.hashtags == tweet_dict['hashtags']
    assert test_tweet.date == 'datum'
