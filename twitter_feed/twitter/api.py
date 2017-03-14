from twitter_feed.mock.tweets import HOME_TIMELINE


class MockAPI:

    def get_home_timeline(self):
        return HOME_TIMELINE
