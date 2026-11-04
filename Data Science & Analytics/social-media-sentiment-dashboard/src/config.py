import json
import os

def load_config(config_path: str = None) -> dict:
    """
    Load social accounts configuration from a JSON file.
    """
    if not config_path:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "..", "config", "social_accounts.json")
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config