from twitter_feed.core.serializers.tweet_serializer import tweets_to_atom


def test_tweets_to_atom_full():
    tweets_dict = [
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

    atom_feed = tweets_to_atom(tweets, 'test.com/feed', 'test.com')

    