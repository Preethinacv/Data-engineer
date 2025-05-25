import json
import pandas as pd

# def transform_data(raw_data):
#     data = []
#     # for item in raw_data:
#     for item in raw_data.get("items", []):

#         if "videoId" in item["id"]:
#             data.append({
#                 "video_id": item["id"]["videoId"],
#                 "title": item["snippet"]["title"],
#                 "description": item["snippet"]["description"],
#                 "published_at": item["snippet"]["publishedAt"]
#             })
#     return pd.DataFrame(data)
import json
import pandas as pd

import pandas as pd

def transform_data(raw_data):
    data = []
    print("Raw data received:", json.dumps(raw_data, indent=2))  # 👈 Print full raw JSON (optional)
    
    for item in raw_data.get("items", []):
        print("\nProcessing item:", json.dumps(item, indent=2))  # 👈 Print each item for inspection

        video_id = item.get("id", {}).get("videoId")
        snippet = item.get("snippet", {})

        print("Extracted video_id:", video_id)  # 👈 See if video_id exists
        print("Extracted title:", snippet.get("title", ""))  # 👈 Check snippet fields

        if video_id:
            data.append({
                "video_id": video_id,
                "title": snippet.get("title", ""),
                "description": snippet.get("description", ""),
                "published_at": snippet.get("publishedAt", "")
            })

    print("\nFinal extracted data:", data)  # 👈 Show what you're returning
    return pd.DataFrame(data)

# Main block
if __name__ == "__main__":
    print("🚀 Running script correctly!")

    try:
        print("🟢 Script started")
        with open("youtube_raw_2025-05-25T04:57:44.259172.json", "r") as f:
            raw_json = json.load(f)
        print("📦 JSON loaded")

        raw_data = raw_json.get("items", [])
        print(f"🔍 Found {len(raw_data)} items")

        df = transform_data(raw_data)
        print(type(df))  # Confirm it's a DataFrame

        df.to_csv("youtube_videos.csv", index=False)
        print("✅ Saved to CSV")
    except Exception as e:
        print("❌ Error occurred:", e)
