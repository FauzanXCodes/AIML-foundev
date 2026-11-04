import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class TikTokFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from TikTok API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 7 TikTok video entries.
        for i in range(7):
            post = SocialPost(
                platform="TikTok",
                post_id=f"tt_{i}",
                content=f"Simulated TikTok video content number {i} with #tiktok{i} and creative effects.",
                timestamp=datetime.now(),
                likes=random.randint(50, 2000),
                retweets=0,
                comments=random.randint(0, 150)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} TikTok video entries")
        return posts