from google.cloud import storage
from transform import transform_data
import json, io
from datetime import datetime
def transform(request):
    print("Starting transformation...")  # Step 1

    bucket_name = "test_etl_youtubr"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blobs = list(bucket.list_blobs(prefix='raw/'))
    if not blobs:
        print("No blobs found!")
        return "No raw files found in GCS."

    latest_blob = sorted(blobs, key=lambda x: x.updated, reverse=True)[0]
    print(f"Latest blob found: {latest_blob.name}")  # Step 2

    content = latest_blob.download_as_text()
    print("Downloaded content length:", len(content))  # Step 3

    raw_data = json.loads(content)
    print("Parsed JSON keys:", raw_data.keys())  # Step 4

    df = transform_data(raw_data)
    print("Transformed DataFrame shape:", df.shape)  # Step 5

    output_filename = f'processed/youtube_transformed_{datetime.utcnow().isoformat()}.csv'
    output_blob = bucket.blob(output_filename)
    output_blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')

    print("Transformation complete.")
    return f"Transformed and stored as {output_filename}"


    # output_filename = f'processed/youtube_transformed_{datetime.utcnow().isoformat()}.csv'
    # output_blob = bucket.blob(output_filename)
    # output_blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')

    # return f"Transformed and stored as {output_filename}"
