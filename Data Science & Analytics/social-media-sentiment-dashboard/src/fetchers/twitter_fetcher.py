import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class TwitterFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Twitter API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 10 tweets with increasing complexity.
        for i in range(10):
            post = SocialPost(
                platform="Twitter",
                post_id=f"tw_{i}",
                content=f"This is a simulated tweet content number {i} with #hashtag{i} and some more details.",
                timestamp=datetime.now(),
                likes=random.randint(10, 500),
                retweets=random.randint(0, 100),
                comments=random.randint(0, 50)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} tweets")
        return posts