import feedparser
import json
import os

RSS_URLS = [
    "https://www.mk.co.kr/rss/50300009/",
    "https://rss.hankyung.com/feed/realestate.xml"
]


def collect_news():
    news_list = []

    for url in RSS_URLS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            news_list.append({
                "title": getattr(entry, "title", ""),
                "link": getattr(entry, "link", ""),
                "published": getattr(entry, "published", "")
            })

    # 제목 기준 중복 제거
    seen_titles = set()
    unique_news = []

    for news in news_list:
        title = news["title"].strip()

        if title and title not in seen_titles:
            seen_titles.add(title)
            unique_news.append(news)

    return unique_news


def save_news(news_list):
    os.makedirs("data", exist_ok=True)

    with open(
        "data/news.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            news_list,
            f,
            ensure_ascii=False,
            indent=4
        )