# 🎵 Spotify Data Pipeline Project

This project implements a **modern serverless data pipeline** for processing Spotify music data extracted from Kaggle. The solution follows best practices in Data Engineering, using **Python and AWS services (S3, Lambda, Secrets Manager, Glue, Athena)**, along with **interactive data visualization in Power BI**.

---

## 📌 Project Goal

The main goal is to build a scalable and modular data pipeline to **extract, transform, and load (ETL)** music-related data into an analytical structure, allowing for insightful analysis and visualization.

---

## 🧭 Architecture Overview

![Spotify_Architecture drawio](https://github.com/user-attachments/assets/2f813a03-9fae-4f21-949f-a1fd36431c79)


```text 
[Data Source (Spotify - Kaggle)]
        |
        ▼
[S3 - Raw Layer]
        |
        ▼
[AWS Lambda - ETL (raw → staging)]
        |
        ▼
[S3 - Staging Layer]
        |
        ▼
[AWS Lambda - ETL (staging → analytics)]
        |
        ▼
[S3 - Analytics Layer]
        |
        ▼
[Glue - Data Catalog]
        |
        ▼
[Athena]
        |
        ▼
[Power BI]

⚙️ Technologies Used

Kaggle – Spotify dataset source

Python – Development of ETL scripts

AWS S3 – Layered data storage (Raw, Staging, Analytics)

AWS Lambda (Serverless) – Data transformation and automation

AWS Glue Data Catalog – Central metadata repository for data

AWS Athena – SQL querying over data stored in S3

AWS CLI – AWS resource management from terminal

Power BI – Interactive data reporting and visualization

🧱 Project Structure

Spotify_Data_Engineer_Project/
└── src/
    ├── .env                                  # Environment variables (not versioned)
    ├── config/
    │   └── settings.py                       # Project configurations
    ├── etl/
    │   ├── spotify_etl_raw_to_staging.py
    │   ├── spotify_etl_staging_to_analytics.py
    │   └── modules/                          # Transformations
    │       ├── tracks_raw_to_staging.py
    │       ├── album_raw_to_staging.py
    │       └── artist_raw_to_staging.py
    ├── scripts/
    │   ├── run_raw_to_staging.py             # Execute ETL spotify_etl_raw_to_staging
    │   └── run_staging_to_analytics.py       # Execute ETL spotify_etl_staging_to_analytics
    ├── handler_raw_to_staging
    ├── handler_staging_to_analytics

🔁 ETL Flow
1. Extraction
Data is manually downloaded from Kaggle and uploaded to the Raw Layer (S3).

2. Transformation
Lambda functions process and clean data from Raw to Staging.

A second transformation stage handles the conversion from Staging to Analytics Layer.

3. Loading
Processed data is stored in the Analytics Layer (S3) for querying and visualization.

4. Cataloging (Glue Data Catalog)
Metadata about the processed data in the Analytics Layer (S3) is defined in the AWS Glue Data Catalog. This involves creating a table that points to the data's location and describes its schema, enabling services like Athena to understand and query the data.

5. Query & Visualization
Athena enables SQL querying on top of S3-stored data.

Power BI connects to Athena for dynamic dashboard creation.

📊 Data Visualization (Power BI)
![spotify_dashboard_screenshot](https://github.com/user-attachments/assets/f4207650-f980-41c1-840a-c12555834c5f)


