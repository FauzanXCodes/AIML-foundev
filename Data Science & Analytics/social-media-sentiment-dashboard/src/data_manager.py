import json
import os
import logging
from datetime import datetime
from models.social_post import SocialPost

def save_data(platform, posts, directory="data"):
    """
    Save the list of posts for a given platform into a JSON file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{platform}_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    data = [post.__dict__ for post in posts]
    with open(filename, 'w') as f:
        json.dump(data, f, default=str, indent=4)
    logging.info(f"Data for {platform} saved to {filename}")

def load_data(platform, directory="data"):
    """
    Load and reconstruct posts for a given platform from JSON files in the specified directory.
    """
    all_posts = []
    if not os.path.exists(directory):
        logging.info("Data directory does not exist. Returning empty list.")
        return all_posts
    data_files = [f for f in os.listdir(directory) if f.startswith(platform)]
    for file in data_files:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r') as f:
            posts_data = json.load(f)
            for pd in posts_data:
                # Reconstruct SocialPost objects (timestamp remains as string)
                post = SocialPost(
                    platform=pd.get("platform"),
                    post_id=pd.get("post_id"),
                    content=pd.get("content"),
                    timestamp=pd.get("timestamp"),
                    likes=pd.get("likes"),
                    retweets=pd.get("retweets"),
                    comments=pd.get("comments"),
                    sentiment=pd.get("sentiment")
                )
                all_posts.append(post)
    logging.info(f"Loaded {len(all_posts)} posts for platform {platform}")
    return all_posts