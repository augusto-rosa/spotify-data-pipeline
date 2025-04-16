"""
Spotify ETL Pipeline: Raw to Staging

This script executes the Extract, Transform, Load (ETL) process to move Spotify data 
from raw format to staging tables.

Usage:
    python scripts/run_raw_to_staging.py

Dependencies:
    - Project configuration in /config/settings
    - Python modules in /etl and /modules
"""
import sys
from pathlib import Path
from etl import spotify_etl_raw_to_staging

# Set project root directory (two levels up from this file)
# Ensures consistent imports regardless of execution location
ROOT_DIR = Path(__file__).resolve().parent.parent

# Add root directory to Python path for absolute imports
sys.path.append(str(ROOT_DIR))

# Main ETL function import (absolute import after modifying sys.path)

def main():
    spotify_etl_raw_to_staging.run_etl_raw_to_staging()

if __name__ == "__main__":
    main()