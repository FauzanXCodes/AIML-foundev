import unittest
from datetime import datetime
from src.models.social_post import SocialPost
from analytics.sentiment_analysis import SentimentAnalyzer, sentiment_distribution
from analytics.trend_analysis import compute_trending_topics
from analytics.metrics import compute_metrics_for_platform

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Create a set of synthetic social posts
        self.posts = []
        for i in range(10):
            content = ("This is a test post with hashtag #test and positive sentiment" 
                       if i % 2 == 0 else "Negative sentiment post #fail")
            post = SocialPost(
                platform="TestPlatform",
                post_id=f"test_{i}",
                content=content,
                timestamp=datetime.now(),
                likes=10,
                retweets=2,
                comments=1
            )
            self.posts.append(post)

    def test_sentiment_analysis(self):
        analyzer = SentimentAnalyzer()
        score = analyzer.analyze(self.posts[0].content)
        self.assertIsInstance(score, float)

    def test_trend_analysis(self):
        trending = compute_trending_topics(self.posts, top_n=3)
        self.assertIsInstance(trending, list)
        self.assertTrue(len(trending) <= 3)

    def test_metrics_computation(self):
        metrics = compute_metrics_for_platform(self.posts)
        self.assertIn("total_posts", metrics)
        self.assertIn("avg_sentiment", metrics)
        self.assertIn("trending", metrics)
        self.assertIn("sentiment_distribution", metrics)

    def test_sentiment_distribution(self):
        # First, analyze sentiment for each post.
        analyzer = SentimentAnalyzer()
        for post in self.posts:
            post.sentiment = analyzer.analyze(post.content)
        dist = sentiment_distribution(self.posts)
        self.assertIn("negative", dist)
        self.assertIn("neutral", dist)
        self.assertIn("positive", dist)

if __name__ == '__main__':
    unittest.main()