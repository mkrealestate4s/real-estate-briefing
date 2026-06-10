from news_classifier import classify_news
from rss_collector import collect_news, save_news
from briefing_generator import generate_html
import os

def main():

    news = collect_news()

    save_news(news)

    categories = classify_news(news)

    for category, items in categories.items():
        print(category, len(items))

    html = generate_html(
        total_count=len(news),
        categories=categories,
    )

    # main.py 위치 기준으로 docs/index.html 경로 고정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "docs", "index.html")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"저장 시도 경로: {output_path}")  # ← 이 줄 추가

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {output_path} 저장 완료")
    print(f"뉴스 {len(news)}건 처리 완료")


if __name__ == "__main__":
    main()