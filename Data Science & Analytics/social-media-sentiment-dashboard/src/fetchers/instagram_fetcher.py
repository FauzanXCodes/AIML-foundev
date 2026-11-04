import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class InstagramFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Instagram API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 12 Instagram posts.
        for i in range(12):
            post = SocialPost(
                platform="Instagram",
                post_id=f"ig_{i}",
                content=f"Simulated Instagram post content number {i} featuring #insta{i} and vibrant visuals.",
                timestamp=datetime.now(),
                likes=random.randint(30, 1000),
                retweets=0,
                comments=random.randint(0, 100)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Instagram posts")
        return posts