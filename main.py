from news_classifier import classify_news
from rss_collector import collect_news, save_news
from html_generator import generate_html

def main():

    news = collect_news()

    save_news(news)

    categories = classify_news(news)

    for category, items in categories.items():
        print(category, len(items))

    generate_html(categories)

    print(f"\n뉴스 {len(news)}건 처리 완료")


if __name__ == "__main__":
    main()