import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class RedditFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Reddit API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 9 Reddit posts.
        for i in range(9):
            post = SocialPost(
                platform="Reddit",
                post_id=f"rd_{i}",
                content=f"Simulated Reddit post content number {i} with community insights and #reddit{i}.",
                timestamp=datetime.now(),
                likes=random.randint(10, 800),
                retweets=0,
                comments=random.randint(0, 70)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Reddit posts")
        return posts