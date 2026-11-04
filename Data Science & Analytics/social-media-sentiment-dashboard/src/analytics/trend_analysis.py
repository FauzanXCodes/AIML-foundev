import re
from collections import Counter
from models.social_post import SocialPost
from utils import setup_logger

def extract_hashtags(text):
    """
    Extract all hashtags from the provided text.
    """
    return re.findall(r"#(\w+)", text)

def compute_trending_topics(posts, top_n=5):
    """
    Compute the top N trending topics based on hashtags found in the posts.
    """
    logger = setup_logger("TrendAnalysis")
    logger.info("Computing trending topics from posts.")
    hashtags = []
    for post in posts:
        hashtags.extend(extract_hashtags(post.content))
    counter = Counter(hashtags)
    trending = counter.most_common(top_n)
    logger.info(f"Trending topics computed: {trending}")
    return trending