from pathlib import Path
import yaml
from dotenv import load_dotenv

import os

PROJECT_ROOT = Path.cwd()
load_dotenv(PROJECT_ROOT / ".env")
CONFIG_PATH = PROJECT_ROOT / os.environ["CONFIG_PATH"]

def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_paddleocr_config() -> dict:
    return load_config()["paddleocr"]