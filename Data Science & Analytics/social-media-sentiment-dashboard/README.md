A demonstration-grade solution: full-stack data analytics platform leveraging REST API integrations, sentiment and trend analysis and real-time interactive dashboards built with Python, Flask and Dash, aggregating social media data from Twitter, Facebook, Instagram, Discord, Medium, Reddit, YouTube and TikTok for marketing insights.

The project was developed as part of my freelance project, which was published with the client's permission. In this release, all sensitive data has been replaced with synthetic examples to ensure the privacy of the freelance client and their customers.

Some features:
- **Multi-platform data aggregation**  
Integrates data fetching from multiple social media platforms using simulated API calls.
- **Advanced analytics**  
Performs sentiment analysis using NLTK's VADER, computes trending topics from hashtags and calculates key performance metrics.
- **Real-time dashboard**  
Interactive dashboard displaying real-time metrics and visualizations using Plotly Dash.
- **Scheduling & automation**  
Uses APScheduler to automatically refresh and update data.
- **Data management**  
Saves and reloads historical data records.
- **Modular & tested**  
Well-structured codebase with dedicated modules for fetchers, analytics, models and utility functions along with unit tests.

## Technologies
- Python 3.x, Flask, Dash, APScheduler
- Pandas, NumPy for data processing
- Requests for simulated API calls
- NLTK for sentiment analysis
- Standard Python logging, unittest for tests

## Structure
```
.
├── README.md
├── .gitignore
├── requirements.txt
├── config/
│   └── social_accounts.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── scheduler.py
│   ├── utils.py
│   ├── dashboard.py
│   ├── data_manager.py
│   ├── fetchers/
│   │   ├── __init__.py
│   │   ├── twitter_fetcher.py
│   │   ├── facebook_fetcher.py
│   │   ├── instagram_fetcher.py
│   │   ├── discord_fetcher.py
│   │   ├── medium_fetcher.py
│   │   ├── reddit_fetcher.py
│   │   ├── youtube_fetcher.py
│   │   └── tiktok_fetcher.py
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── sentiment_analysis.py
│   │   ├── trend_analysis.py
│   │   └── metrics.py
│   └── models/
│       ├── __init__.py
│       ├── social_post.py
│       └── account.py
└── tests/
    ├── test_fetchers.py
    └── test_analytics.py
```

## How to run
1. Clone the repository
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Update `config/social_accounts.json` with your social media account details.
4. Start the app:
   ```
   python src/main.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:8050` to view the dashboard.

## Testing
Run tests using:
```
pytest tests/
```

## To do
TBA

## Contributions
are welcome

## License
Apache 2.0
