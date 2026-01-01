import os
from pathlib import Path 

DEFAULT_DB_NAME = "lc_dashboard.sqlite"

def db_path() -> str: 
    override = os.getenv("LCDASH_DB_PATH")
    if override: 
        return override 
    return str(Path.cwd() / DEFAULT_DB_NAME)

