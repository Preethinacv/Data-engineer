## YouTube ETL Pipeline on Google Cloud

##### What the Project is About

This project is an end-to-end YouTube ETL (Extract, Transform, Load) pipeline built using Python and Google Cloud Platform services.

#####  This project implements a complete YouTube ETL pipeline that retrieves video metadata from a specific YouTube channel via the YouTube Data API. It processes the extracted data into a well-structured CSV format and saves both the original raw JSON files and the transformed CSV files in Google Cloud Storage. The pipeline takes the YouTube channel ID—a unique identifier for each channel—along with an API key as inputs to fetch detailed information about the latest videos, including video ID, title, description, and publish date.


###### Setup Instructions

- Enable required GCP APIs: YouTube Data API v3, Cloud Functions, Cloud Storage, BigQuery, Secret Manager, etc.
- Create and configure GCS buckets.
- Set environment variables or config files with API keys and bucket names.
- Deploy cloud functions for extraction and transformation.
