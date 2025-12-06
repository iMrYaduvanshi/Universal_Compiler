import json
import os
import sys


def resource_path(relative_path):
    """
    Get absolute path to resource (works for dev and for PyInstaller EXE)
    """
    try:
        # PyInstaller stores files inside _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_config():
    config_file = resource_path(os.path.join("config", "compilers.json"))

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"compilers.json missing: {config_file}")

    with open(config_file, "r") as f:
        return json.load(f)
