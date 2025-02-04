import os
from dotenv import load_dotenv
from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

class Config:
    def __init__(self):
        self.settings = self._load_config()
        
    def _load_config(self):
        with open(BASE_DIR / "config.yaml") as f:
            return yaml.safe_load(f)
    
    def get(self, key, default=None):
        return os.getenv(key, self.settings.get(key, default))

config = Config() 