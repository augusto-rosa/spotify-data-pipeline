"""
Spotify ETL Pipeline: Staging to Analytics

Transforms staged data into analytical-ready table.
Designed for daily execution after the raw-to-staging ETL completes.

Usage:
    python scripts/run_staging_to_analytics.py

Dependencies:
    - Processed data must exist in staging
    - Depends on transformations defined in /etl/spotify_etl_staging_to_analytics.py
"""
import sys
from pathlib import Path
from etl import spotify_etl_staging_to_analytics
# Establish absolute project root path (two levels up from this file)
# Critical for consistent imports across different execution contexts
ROOT_DIR = Path(__file__).resolve().parent.parent

# Add root directory to Python path for absolute imports
sys.path.append(str(ROOT_DIR))

# Main ETL function import (absolute import after modifying sys.path)
def main():
    spotify_etl_staging_to_analytics.run_etl_staging_to_analytics()

if __name__ == "__main__":
    main()