import unittest
from src.fetchers.twitter_fetcher import TwitterFetcher
from src.fetchers.facebook_fetcher import FacebookFetcher
from src.fetchers.instagram_fetcher import InstagramFetcher
from src.fetchers.discord_fetcher import DiscordFetcher
from src.fetchers.medium_fetcher import MediumFetcher
from src.fetchers.reddit_fetcher import RedditFetcher
from src.fetchers.youtube_fetcher import YouTubeFetcher
from src.fetchers.tiktok_fetcher import TikTokFetcher

class TestFetchers(unittest.TestCase):
    def setUp(self):
        # Minimal (synthetic) config for fetchers
        self.config = {}

    def test_twitter_fetcher(self):
        fetcher = TwitterFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_facebook_fetcher(self):
        fetcher = FacebookFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_instagram_fetcher(self):
        fetcher = InstagramFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_discord_fetcher(self):
        fetcher = DiscordFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_medium_fetcher(self):
        fetcher = MediumFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_reddit_fetcher(self):
        fetcher = RedditFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_youtube_fetcher(self):
        fetcher = YouTubeFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_tiktok_fetcher(self):
        fetcher = TikTokFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()