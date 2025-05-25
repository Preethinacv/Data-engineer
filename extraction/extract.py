import json
from googleapiclient.discovery import build

# def fetch_videos(api_key, channel_id, max_results=10):
#     youtube = build("youtube", "v3", developerKey=api_key)
#     request = youtube.search().list(
#         part="snippet",
#         channelId=channel_id,
#         maxResults=max_results,
#         order="date"
#     )
#     response = request.execute()
#     return response['items']
def fetch_videos(api_key, channel_id):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=10,
        order="date"
    )
    response = request.execute()
    print("✅ API call successful. Videos fetched.")
    videos =response.get("items", [])
    # return response.get("items", [])
    print(f"✅ API call successful. Videos fetched: {len(videos)} items.")
    return videos