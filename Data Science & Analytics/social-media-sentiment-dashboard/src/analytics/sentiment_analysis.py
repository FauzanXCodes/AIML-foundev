import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from models.social_post import SocialPost
from utils import setup_logger

# Ensure that VADER lexicon is available.
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.logger = setup_logger(self.__class__.__name__)

    def analyze(self, text: str) -> float:
        """
        Analyze the sentiment of the given text and return the compound score.
        """
        self.logger.info("Analyzing sentiment for text.")
        scores = self.analyzer.polarity_scores(text)
        return scores['compound']

def analyze_posts_sentiment(posts):
    """
    Apply sentiment analysis to a list of SocialPost objects.
    """
    analyzer = SentimentAnalyzer()
    for post in posts:
        post.sentiment = analyzer.analyze(post.content)
    return posts

def sentiment_distribution(posts):
    """
    Compute sentiment distribution over a list of posts.
    Returns a dictionary with counts for negative, neutral and positive sentiments.
    """
    distribution = {"negative": 0, "neutral": 0, "positive": 0}
    for post in posts:
        score = post.sentiment
        if score < -0.05:
            distribution["negative"] += 1
        elif score > 0.05:
            distribution["positive"] += 1
        else:
            distribution["neutral"] += 1
    return distribution