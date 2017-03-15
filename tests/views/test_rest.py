import json
import pytest

import dateutil
import feedparser

from twitter_feed import make_app
from twitter_feed.core.tweet import Tweet
from twitter_feed.mock.tweets import HOME_TIMELINE, USER_TIMELINE


@pytest.fixture
def rest_app():
    return make_app(api='dev')


@pytest.fixture
def test_client(rest_app):
    return rest_app.test_client()


def test_home_timeline(test_client):
    response = test_client.get('/rest/')
    feed = feedparser.parse(response.data)
    tweets = Tweet.tweets_from_list(HOME_TIMELINE)

    assert feed.feed.title == 'Home feed'

    for entry, tweet in zip(feed.entries, tweets):
        assert entry.author == tweet.user.screen_name
        assert entry.title == tweet.user.name

        date_feed = dateutil.parser.parse(entry.published)
        assert date_feed == tweet.date
        date_feed = dateutil.parser.parse(entry.updated)
        assert date_feed == tweet.date

        assert entry.id == 'urn:twitter_id:' + tweet.id_

        dict_content = tweet.text + '<br>'
        dict_content += '<b>Mentions:</b> '
        for mention in tweet.mentions:
            dict_content += mention.name + '; '
        dict_content += '<br>'
        dict_content += '<b>Hashtags:</b> '
        for hashtag in tweet.hashtags:
            dict_content += hashtag.text + '; '
        assert entry.content[0].value == dict_content.strip()


def test_user_timeline(test_client):
    response = test_client.get('/rest/users/test')
    feed = feedparser.parse(response.data)
    tweets = Tweet.tweets_from_list(USER_TIMELINE)

    assert feed.feed.title == 'Feed for test'

    for entry, tweet in zip(feed.entries, tweets):
        assert entry.author == tweet.user.screen_name
        assert entry.title == tweet.user.name

        date_feed = dateutil.parser.parse(entry.published)
        assert date_feed == tweet.date
        date_feed = dateutil.parser.parse(entry.updated)
        assert date_feed == tweet.date

        assert entry.id == 'urn:twitter_id:' + tweet.id_

        dict_content = tweet.text + '<br>'
        dict_content += '<b>Mentions:</b> '
        for mention in tweet.mentions:
            dict_content += mention.name + '; '
        dict_content += '<br>'
        dict_content += '<b>Hashtags:</b> '
        for hashtag in tweet.hashtags:
            dict_content += hashtag.text + '; '
        assert entry.content[0].value == dict_content.strip()


def test_hashtag_timeline(test_client):
    response = test_client.get('/rest/hashtags/test')
    feed = feedparser.parse(response.data)
    tweets = Tweet.tweets_from_list(USER_TIMELINE)

    assert feed.feed.title == 'Feed for test'

    for entry, tweet in zip(feed.entries, tweets):
        assert entry.author == tweet.user.screen_name
        assert entry.title == tweet.user.name

        date_feed = dateutil.parser.parse(entry.published)
        assert date_feed == tweet.date
        date_feed = dateutil.parser.parse(entry.updated)
        assert date_feed == tweet.date

        assert entry.id == 'urn:twitter_id:' + tweet.id_

        dict_content = tweet.text + '<br>'
        dict_content += '<b>Mentions:</b> '
        for mention in tweet.mentions:
            dict_content += mention.name + '; '
        dict_content += '<br>'
        dict_content += '<b>Hashtags:</b> '
        for hashtag in tweet.hashtags:
            dict_content += hashtag.text + '; '
        assert entry.content[0].value == dict_content.strip()
