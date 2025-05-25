from google.cloud import storage
from transform import transform_data
import json, io
from datetime import datetime
def transform(request):
    bucket_name = "YOUR_GCS_BUCKET_NAME"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blobs = list(bucket.list_blobs(prefix='raw/'))
    if not blobs:
        return "No raw files found in GCS."

    latest_blob = sorted(blobs, key=lambda x: x.updated, reverse=True)[0]

    content = latest_blob.download_as_text()

    raw_data = json.loads(content)

    df = transform_data(raw_data)

    output_filename = f'processed/youtube_transformed_{datetime.utcnow().isoformat()}.csv'
    output_blob = bucket.blob(output_filename)
    output_blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')

    return f"Transformed and stored as {output_filename}"

