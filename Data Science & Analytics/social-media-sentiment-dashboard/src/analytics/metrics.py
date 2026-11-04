from analytics.sentiment_analysis import analyze_posts_sentiment, sentiment_distribution
from analytics.trend_analysis import compute_trending_topics
from utils import setup_logger

def compute_metrics_for_platform(posts):
    """
    Compute metrics such as total posts, average sentiment and trending topics for a given list of posts.
    """
    logger = setup_logger("Metrics")
    logger.info("Computing metrics for a platform.")
    if not posts:
        return {"total_posts": 0, "avg_sentiment": 0, "trending": []}
    posts = analyze_posts_sentiment(posts)
    total_posts = len(posts)
    avg_sentiment = sum(post.sentiment for post in posts) / total_posts
    trending = compute_trending_topics(posts)
    sentiment_dist = sentiment_distribution(posts)
    metrics = {
        "total_posts": total_posts,
        "avg_sentiment": avg_sentiment,
        "trending": trending,
        "sentiment_distribution": sentiment_dist
    }
    logger.info(f"Metrics computed: {metrics}")
    return metrics

def compute_overall_metrics(all_data):
    """
    Compute overall metrics for each platform from the aggregated data.
    """
    overall = {}
    for platform, posts in all_data.items():
        overall[platform] = compute_metrics_for_platform(posts)
    return overall