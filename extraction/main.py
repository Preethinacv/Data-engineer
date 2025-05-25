# import os, json
# from datetime import datetime
# from google.cloud import storage
# from extract import fetch_videos

# def youtube_extract(request):
#     with open("config/config.json") as f:
#         config = json.load(f)

#     videos = fetch_videos(config["api_key"], config["channel_id"])
#     filename = f'youtube_raw_{datetime.utcnow().isoformat()}.json'

#     client = storage.Client()
#     bucket = client.bucket(config["bucket_name"])
#     blob = bucket.blob(f'raw/{filename}')
#     blob.upload_from_string(json.dumps(videos), content_type='application/json')
#     print(f"✅ File {filename} uploaded to raw/ in bucket {config['bucket_name']}")

#     return "Extraction Successful!"
import os, json
from datetime import datetime
from google.cloud import storage
from extract import fetch_videos

def youtube_extract():
    with open("config/config.json") as f:
        config = json.load(f)

    videos = fetch_videos(config["api_key"], config["channel_id"])

    if not videos:
        return

    filename = f'youtube_raw_{datetime.utcnow().isoformat()}.json'

    client = storage.Client()
    bucket = client.bucket(config["bucket_name"])
    blob = bucket.blob(f'raw/{filename}')
    blob.upload_from_string(json.dumps(videos), content_type='application/json')



if __name__ == "__main__":
    youtube_extract()
