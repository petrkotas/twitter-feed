import datetime

from twitter_feed.core.tweet import Tweet
from twitter_feed.core.user import User
from twitter_feed.core.hashtag import Hashtag


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
        'entities': {
            'user_mentions': [
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
    }

    test_tweet = Tweet.from_dict(tweet_dict)

    assert test_tweet.id_ == tweet_dict['id_str']
    assert test_tweet.text == tweet_dict['text']
    assert test_tweet.user == User.from_dict(tweet_dict['user'])

    assert len(test_tweet.mentions) == len(tweet_dict['entities']['user_mentions'])
    for user_mention, mention in zip(test_tweet.mentions, tweet_dict['entities']['user_mentions']):
        assert user_mention == User.from_dict(mention)

    assert len(test_tweet.hashtags) == len(tweet_dict['entities']['hashtags'])
    for tweet_hashtag, hashtag in zip(test_tweet.hashtags, tweet_dict['entities']['hashtags']):
        assert tweet_hashtag == Hashtag.from_dict(hashtag)

    assert test_tweet.date == datetime.datetime.strptime(tweet_dict['created_at'], '%a %b %d %X %z %Y')


def test_tweet_incomplete():
    tweet_dict = {
        'created_at': 'Tue Aug 28 21:16:23 +0000 2012',
        'text': 'just another test',
        'user': {
            'name': 'OAuth Dancer',
            'screen_name': 'oauth_dancer',
            'id_str': '119476949',
        },
        'entities': {
            'user_mentions': [
                {
                    'name': 'Cal',
                    'id_str': '17445752'
                }
            ],
            'hashtags': [
                {
                    'text': 'twitter'
                }
            ]
        }
    }

    test_tweet = Tweet.from_dict(tweet_dict)

    assert test_tweet.id_ is None
    assert test_tweet.text == tweet_dict['text']
    assert test_tweet.user == User.from_dict(tweet_dict['user'])

    assert len(test_tweet.mentions) == len(tweet_dict['entities']['user_mentions'])
    for user_mention, mention in zip(test_tweet.mentions, tweet_dict['entities']['user_mentions']):
        assert user_mention == User.from_dict(mention)

    assert len(test_tweet.hashtags) == len(tweet_dict['entities']['hashtags'])
    for tweet_hashtag, hashtag in zip(test_tweet.hashtags, tweet_dict['entities']['hashtags']):
        assert tweet_hashtag == Hashtag.from_dict(hashtag)

    assert test_tweet.date == datetime.datetime.strptime(tweet_dict['created_at'], '%a %b %d %X %z %Y')


def test_tweet_list():
    tweets_list = [
        {
            'created_at': 'Tue Aug 28 21:16:23 +0000 2012',
            'id_str': '240558470661799936',
            'entities': {
                'urls': [
                ],
                'hashtags': [
                    {
                        'text': 'bagr'
                    }
                ],
                'user_mentions': [
                    {
                        'name': 'OAuth Dancer',
                        'screen_name': 'oauth_dancer',
                        'id_str': '119476949',
                    }
                ]
            },
            'text': 'just another test',
            'source': 'OAuth Dancer Reborn',
            'user': {
                'name': 'OAuth Dancer',
                'created_at': 'Wed Mar 03 19:37:35 +0000 2010',
                'id_str': '119476949',
                'screen_name': 'oauth_dancer'
            },
        },
        {
            'created_at': 'Tue Aug 28 21:16:23 +0000 2012',
            'id_str': '240558470661799936',
            'entities': {
                'urls': [
                ],
                'hashtags': [
                    {
                        'text': 'bagr'
                    }
                ],
                'user_mentions': [
                    {
                        'name': 'OAuth Dancer',
                        'screen_name': 'oauth_dancer',
                        'id_str': '119476949',
                    }
                ]
            },
            'text': 'just another test',
            'source': 'OAuth Dancer Reborn',
            'user': {
                'name': 'OAuth Dancer',
                'created_at': 'Wed Mar 03 19:37:35 +0000 2010',
                'id_str': '119476949',
                'screen_name': 'oauth_dancer'
            },
        }
    ]

    tweets = Tweet.tweets_from_list(tweets_list)

    for tweet, tweet_dict in zip(tweets, tweets_list):
        assert tweet == Tweet.from_dict(tweet_dict)
