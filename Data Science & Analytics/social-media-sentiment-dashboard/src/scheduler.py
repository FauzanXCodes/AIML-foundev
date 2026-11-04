from apscheduler.schedulers.background import BackgroundScheduler
import logging
from fetchers import twitter_fetcher, facebook_fetcher, instagram_fetcher, discord_fetcher, medium_fetcher, reddit_fetcher, youtube_fetcher, tiktok_fetcher
from analytics import metrics
from data_manager import save_data
import datetime

def fetch_all_data(config):
    logging.info("Starting data fetch cycle")
    
    # Instantiate each fetcher with its configuration details.
    twitter_data = twitter_fetcher.TwitterFetcher(config.get("twitter", {})).get_data()
    facebook_data = facebook_fetcher.FacebookFetcher(config.get("facebook", {})).get_data()
    instagram_data = instagram_fetcher.InstagramFetcher(config.get("instagram", {})).get_data()
    discord_data = discord_fetcher.DiscordFetcher(config.get("discord", {})).get_data()
    medium_data = medium_fetcher.MediumFetcher(config.get("medium", {})).get_data()
    reddit_data = reddit_fetcher.RedditFetcher(config.get("reddit", {})).get_data()
    youtube_data = youtube_fetcher.YouTubeFetcher(config.get("youtube", {})).get_data()
    tiktok_data = tiktok_fetcher.TikTokFetcher(config.get("tiktok", {})).get_data()
    
    all_data = {
        "twitter": twitter_data,
        "facebook": facebook_data,
        "instagram": instagram_data,
        "discord": discord_data,
        "medium": medium_data,
        "reddit": reddit_data,
        "youtube": youtube_data,
        "tiktok": tiktok_data
    }
    
    # Save each platform's data to disk
    for platform, posts in all_data.items():
        save_data(platform, posts)
    
    # Process and compute overall metrics
    computed_metrics = metrics.compute_overall_metrics(all_data)
    logging.info("Data fetch cycle completed at {}. Computed Metrics: {}"
                 .format(datetime.datetime.now(), computed_metrics))

def start_scheduler(config):
    scheduler = BackgroundScheduler()
    # Schedule the fetch_all_data job to run every 5 minutes
    scheduler.add_job(fetch_all_data, 'interval', minutes=5, args=[config])
    scheduler.start()
    logging.info("Scheduler started with a 5-minute interval")