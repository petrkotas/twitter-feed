import dateutil.parser
import feedparser

from twitter_feed.core.tweet import Tweet
from twitter_feed.core.serializers.tweet_serializer import tweets_to_atom


def test_tweets_to_atom_full():
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

    atom_feed = tweets_to_atom(tweets, 'My twitter atom feed', 'test.com/feed', 'test.com')
    feed = atom_feed.to_string()

    feed_parsed = feedparser.parse(feed)

    assert feed_parsed.feed.title == 'My twitter atom feed'

    for entry in feed_parsed.entries:
        assert entry.author == tweets_list[0]['user']['screen_name']
        assert entry.title == tweets_list[0]['user']['name']

        date_dict = dateutil.parser.parse(tweets_list[0]['created_at'])
        date_feed = dateutil.parser.parse(entry.published)
        assert date_feed == date_dict
        date_feed = dateutil.parser.parse(entry.updated)
        assert date_feed == date_dict

        assert entry.id == 'urn:twitter_id:' + tweets_list[0]['id_str']

        dict_content = tweets_list[0]['text'] + '<br>'
        dict_content += '<b>Mentions:</b> '
        for mention in tweets_list[0]['entities']['user_mentions']:
            dict_content += mention['name'] + '; '
        dict_content += '<br>'
        dict_content += '<b>Hashtags:</b> '
        for hashtag in tweets_list[0]['entities']['hashtags']:
            dict_content += hashtag['text'] + '; '
        assert entry.content[0].value == dict_content.strip()

