import typing

from twitter_feed.core.tweet import Tweet


def match_tweet_replies(tweet: Tweet, mentions: typing.List[Tweet]) -> typing.List[Tweet]:
    return [tw for tw in mentions if tw.reply_to == tweet.id_]
