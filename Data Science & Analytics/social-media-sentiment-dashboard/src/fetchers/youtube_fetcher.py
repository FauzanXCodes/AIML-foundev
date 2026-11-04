import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class YouTubeFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from YouTube API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 5 YouTube video entries.
        for i in range(5):
            post = SocialPost(
                platform="YouTube",
                post_id=f"yt_{i}",
                content=f"Simulated YouTube video description number {i} with #youtube{i} and video details.",
                timestamp=datetime.now(),
                likes=random.randint(100, 5000),
                retweets=0,
                comments=random.randint(0, 300)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} YouTube video entries")
        return posts