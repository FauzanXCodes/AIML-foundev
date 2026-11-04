import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class FacebookFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Facebook API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 8 Facebook posts.
        for i in range(8):
            post = SocialPost(
                platform="Facebook",
                post_id=f"fb_{i}",
                content=f"Simulated Facebook post content number {i} with interesting insights #fb{i}.",
                timestamp=datetime.now(),
                likes=random.randint(20, 600),
                retweets=0,
                comments=random.randint(0, 80)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Facebook posts")
        return posts