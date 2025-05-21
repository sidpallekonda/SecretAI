import os
import json
import sys

def get_base_path():
    """
    Determines the base path depending on if the script is frozen (PyInstaller) or not.
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def load_config():
    """
    Loads the config.json file containing the API key.
    """
    base_path = get_base_path()
    config_path = os.path.join(base_path, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config.json not found at {config_path}")

    with open(config_path, "r") as f:
        config = json.load(f)

    if "api_key" not in config:
        raise KeyError("Missing 'api_key' in config.json")

    return config

