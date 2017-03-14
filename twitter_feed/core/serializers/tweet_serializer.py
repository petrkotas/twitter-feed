import typing

from werkzeug.contrib.atom import AtomFeed, FeedEntry

from twitter_feed.core.hashtag import Hashtag
from twitter_feed.core.tweet import Tweet
from twitter_feed.core.user import User


def tweets_to_atom(tweets: typing.List[Tweet], title: str=None, url: str = None, host_url: str = None) -> AtomFeed:
    feed = AtomFeed(title or 'My feed', feed_url=url, url=host_url)

    for tweet in tweets:
        feed_content = tweet.text + '<br>'

        feed_content += '<b>Mentions:</b> '
        for mention in tweet.mentions:  # type:User
            feed_content += mention.name + '; '

        feed_content += '<br>'
        feed_content += '<b>Hashtags:</b> '
        for hashtag in tweet.hashtags:  # type:Hashtag
            feed_content += hashtag.text + '; '

        entry = FeedEntry(
            title=str(tweet.date.date) + tweet.user.name,
            id='urn:twitter_id:' + tweet.id_,
            author={'name': tweet.user.screen_name},
            published=tweet.date,
            updated=tweet.date,
            content_type='html',
            content=feed_content
        )

        feed.add(entry)

    return feed
