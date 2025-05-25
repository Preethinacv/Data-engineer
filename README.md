# YouTube ETL Pipeline on Google Cloud

## What the Project is About

This project is an end-to-end YouTube ETL (Extract, Transform, Load) pipeline built using Python and Google Cloud Platform services.

The pipeline extracts video metadata from a specified YouTube channel using the YouTube Data API, transforms the data into structured CSV files, and stores it in Google Cloud Storage.

## Setup Instructions

- Enable required GCP APIs: YouTube Data API v3, Cloud Functions, Cloud Storage, BigQuery, Secret Manager, etc.
- Create and configure GCS buckets.
- Set environment variables or config files with API keys and bucket names.
- Deploy cloud functions for extraction and transformation.
