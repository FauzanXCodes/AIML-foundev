import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class DiscordFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Discord API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 6 Discord messages.
        for i in range(6):
            post = SocialPost(
                platform="Discord",
                post_id=f"dc_{i}",
                content=f"Simulated Discord message number {i} with #discord{i} mention.",
                timestamp=datetime.now(),
                likes=random.randint(5, 200),
                retweets=0,
                comments=random.randint(0, 30)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Discord messages")
        return posts