import logging
from config import load_config
from scheduler import start_scheduler
from dashboard import create_dashboard_app

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    setup_logging()
    logging.info("Starting social-metrics-dashboard Application")
    
    config = load_config()
    logging.info("Configuration loaded successfully")
    
    # Start scheduler to periodically fetch data and save to disk
    start_scheduler(config)
    
    # Create and run dashboard app
    app = create_dashboard_app(config)
    logging.info("Dashboard app created, starting server")
    app.run_server(debug=True)

if __name__ == '__main__':
    main()