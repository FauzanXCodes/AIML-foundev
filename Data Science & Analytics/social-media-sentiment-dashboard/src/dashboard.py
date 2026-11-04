import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random
import datetime
from utils import setup_logger

# In-memory store for simulated metrics (will update on each callback)
METRICS_STORE = {
    "twitter": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "facebook": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "instagram": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "discord": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "medium": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "reddit": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "youtube": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)},
    "tiktok": {"engagement": random.randint(100, 1000), "sentiment": random.uniform(-1, 1)}
}

def create_dashboard_app(config):
    """
    Create and configure the Dash dashboard application.
    """
    app = dash.Dash(__name__)
    app.title = "social-metrics-dashboard Dashboard"

    app.layout = html.Div([
        html.H1("Social Media Analytics Dashboard", style={'textAlign': 'center'}),
        html.Div(id='last-update', children="Last update: " + str(datetime.datetime.now()), style={'textAlign': 'center', 'marginBottom': '20px'}),
        dcc.Interval(
            id='interval-component',
            interval=5*60*1000,  # every 5 minutes
            n_intervals=0
        ),
        html.Div([
            dcc.Graph(id='engagement-graph')
        ], style={'width': '80%', 'margin': 'auto'}),
        html.Br(),
        html.Div([
            dcc.Graph(id='sentiment-graph')
        ], style={'width': '80%', 'margin': 'auto'}),
        html.Br(),
        html.Div(id='metrics-table', style={'width': '60%', 'margin': 'auto'})
    ], style={'margin': '2%'})

    @app.callback(
        [Output('engagement-graph', 'figure'),
         Output('sentiment-graph', 'figure'),
         Output('last-update', 'children'),
         Output('metrics-table', 'children')],
        [Input('interval-component', 'n_intervals')]
    )
    def update_dashboard(n):
        # Simulate updating metrics with new random data.
        updated_metrics = {}
        for platform in METRICS_STORE.keys():
            updated_metrics[platform] = {
                "engagement": random.randint(100, 1000),
                "sentiment": round(random.uniform(-1, 1), 2)
            }
        METRICS_STORE.update(updated_metrics)
        last_update = "Last update: " + str(datetime.datetime.now())
        
        # Engagement bar chart
        platforms = list(METRICS_STORE.keys())
        engagements = [METRICS_STORE[platform]["engagement"] for platform in platforms]
        engagement_fig = {
            'data': [go.Bar(
                x=platforms,
                y=engagements,
                marker=dict(color='rgb(55, 83, 109)')
            )],
            'layout': go.Layout(
                title='Engagement Metrics by Platform',
                xaxis={'title': 'Platform'},
                yaxis={'title': 'Engagement'}
            )
        }
        
        # Sentiment distribution bar chart
        sentiments = [METRICS_STORE[platform]["sentiment"] for platform in platforms]
        sentiment_fig = {
            'data': [go.Bar(
                x=platforms,
                y=sentiments,
                marker=dict(color='rgb(26, 118, 255)')
            )],
            'layout': go.Layout(
                title='Average Sentiment Score by Platform',
                xaxis={'title': 'Platform'},
                yaxis={'title': 'Sentiment Score'}
            )
        }
        
        # Metrics table creation
        table_rows = []
        for platform, data in METRICS_STORE.items():
            table_rows.append(
                html.Tr([
                    html.Td(platform),
                    html.Td(data["engagement"]),
                    html.Td(data["sentiment"])
                ], style={'border': '1px solid black', 'padding': '5px'})
            )
        table = html.Table([
            html.Thead(html.Tr([html.Th("Platform"), html.Th("Engagement"), html.Th("Sentiment")])),
            html.Tbody(table_rows)
        ], style={'width': '100%', 'borderCollapse': 'collapse', 'textAlign': 'center'})

        return engagement_fig, sentiment_fig, last_update, table

    return app