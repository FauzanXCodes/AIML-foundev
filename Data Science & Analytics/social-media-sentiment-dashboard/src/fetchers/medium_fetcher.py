import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class MediumFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Medium API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 4 Medium articles.
        for i in range(4):
            post = SocialPost(
                platform="Medium",
                post_id=f"md_{i}",
                content=f"Simulated Medium article content number {i} discussing trends and insights #medium{i}.",
                timestamp=datetime.now(),
                likes=random.randint(50, 300),
                retweets=0,
                comments=random.randint(0, 20)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Medium articles")
        return posts