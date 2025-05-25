
import json
import pandas as pd

import pandas as pd

def transform_data(raw_data):
    data = []
    
    for item in raw_data.get("items", []):

        video_id = item.get("id", {}).get("videoId")
        snippet = item.get("snippet", {})

        if video_id:
            data.append({
                "video_id": video_id,
                "title": snippet.get("title", ""),
                "description": snippet.get("description", ""),
                "published_at": snippet.get("publishedAt", "")
            })

    return pd.DataFrame(data)
