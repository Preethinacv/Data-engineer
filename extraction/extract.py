import json
from googleapiclient.discovery import build
def fetch_videos(api_key, channel_id):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=10,
        order="date"
    )
    response = request.execute()
    videos =response.get("items", [])
    return videos
