import feedparser
import json
from datetime import datetime

# 例：ぴあ音楽のRSS
RSS_FEEDS = [
    ("音楽", "https://t.pia.jp/rss/music.xml"),
    # ("スポーツ", "https://t.pia.jp/rss/sports.xml"),
    # （展示や他ジャンルも追加可能）
]

def parse_feed(genre, url):
    feed = feedparser.parse(url)
    events = []
    for entry in feed.entries:
        events.append({
            "title": entry.title,
            "genre": genre,
            "date": entry.get("published", "")[:10],
            "location": "東京都内（詳細URL参照）",
            "url": entry.link
        })
    return events

def main():
    all_events = []
    for genre, url in RSS_FEEDS:
        all_events.extend(parse_feed(genre, url))
    
    with open("data/events.json", "w", encoding="utf-8") as f:
        json.dump(all_events, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
