from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class SocialPost:
    platform: str
    post_id: str
    content: str
    timestamp: any # Using 'any' to allow string (from disk) or datetime
    likes: int
    retweets: int = 0
    comments: int = 0
    sentiment: float = field(default=0.0)