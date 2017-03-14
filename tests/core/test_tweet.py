import datetime

import dateutil.parser

from twitter_feed.core.tweet import Tweet
from twitter_feed.core.user import User
from twitter_feed.core.hashtag import Hashtag
from twitter_feed.mock.tweets import HOME_TIMELINE


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

    assert test_tweet.date == dateutil.parser.parse(tweet_dict['created_at'])


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

    assert test_tweet.date == dateutil.parser.parse(tweet_dict['created_at'])


def test_tweet_list():

    tweets = Tweet.tweets_from_list(HOME_TIMELINE)

    assert len(tweets) == len(HOME_TIMELINE)
    for tweet, tweet_dict in zip(tweets, HOME_TIMELINE):
        assert tweet == Tweet.from_dict(tweet_dict)
