# 🎵 Spotify Data Pipeline Project

This project implements a **modern serverless data pipeline** for processing Spotify music data extracted from Kaggle. The solution follows best practices in Data Engineering, using **Python and AWS services (S3, Lambda, Secrets Manager, Glue, Athena)**, along with **interactive data visualization in Power BI**.

---

## 📌 Project Goal

The main goal is to build a scalable and modular data pipeline to **extract, transform, and load (ETL)** music-related data into an analytical structure, allowing for insightful analysis and visualization.

---

## 🧭 Architecture Overview

![Spotify_Architecture drawio](https://github.com/user-attachments/assets/2f813a03-9fae-4f21-949f-a1fd36431c79)

## 🛰️ Pipeline Overview
``` 
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
```

## 🔧 Why I Built This Project?

I built this project to deepen my hands-on experience with AWS cloud services and Python, focusing on building scalable and automated data pipelines. As an **AWS-certified** professional, I wanted to reinforce my understanding of services like Lambda, S3, Glue, Athena, and EventBridge by implementing a production-like data pipeline architecture.  

Python was chosen as the core language to manage data transformation and orchestration logic due to its flexibility and rich ecosystem for data engineering.  

This project simulates real-world data engineering challenges such as orchestrating data extraction jobs, transforming semi-structured data, and making it queryable through Athena. It reflects common scenarios I encounter in my current role and serves as a practical environment to apply and test cloud-based design patterns and automation techniques.

## ⚙️ Technologies Used

- **Kaggle** – Spotify dataset source
- **Python** – Development of ETL scripts
- **AWS S3** – Layered data storage (Raw, Staging, Analytics)
- **AWS Lambda (Serverless)** – Data transformation and automation
- **AWS Glue** – Central metadata repository for data
- **AWS Athena** – SQL querying over data stored in S3
- **AWS CLI** – AWS resource management from terminal
- **Power BI** – Interactive data reporting and visualization

## 🧱 Project Structure

```bash
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
```
## 🔁 ETL Flow
1. **Extraction**: Data is manually downloaded from Kaggle and uploaded to the Raw Layer (S3).
2. **Transformation**: Lambda functions process and clean data from Raw to Staging. A second transformation stage handles the conversion from Staging to Analytics Layer.
3. **Loading**: Processed data is stored in the Analytics Layer (S3) for querying and visualization.
4. **Cataloging (Glue Data Catalog)**: Metadata about the processed data in the Analytics Layer (S3) is defined in the AWS Glue Data Catalog. This involves creating a table that points to the data's location and describes its schema, enabling services like Athena to understand and query the data.
5. **SQL & Query**: Athena enables SQL querying on top of S3-stored data.
6. **Visualization** Power BI connects to Athena for dynamic dashboard creation.

## 📊 Data Visualization (Power BI)

![spotify_dashboard](https://github.com/user-attachments/assets/53b1b5a3-3b65-44a6-81df-937d1d7bb162)

## ✅ Conclusion and Learnings
This project presented the implementation of a modern data pipeline using **Spotify dataset from Kaggle** as the data source. The pipeline was developed with a focus on cloud-based tools and services to automate the process of storing, cataloging, querying, and visualizing data.

Throughout the project, I had the opportunity to:

Work with **AWS services** such as **S3**, **Lambda Function**s, **Glue**, and **Athena** to build a fully serverless pipeline.

Automate data ingestion and processing using **Python** and **AWS Lambda**, reducing manual intervention.

Organize and register the dataset using **AWS Glue**, enabling easy schema discovery and structured querying.

Analyze the dataset efficiently with **Athena** using standard SQL.

Create a **Power BI dashboard** to explore insights about music trends, popularity, and track characteristics.

This project strengthened my knowledge of **cloud data engineering**, focusing on building scalable, cost-effective, and automated pipelines using the AWS ecosystem.

