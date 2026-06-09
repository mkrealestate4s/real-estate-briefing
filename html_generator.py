import os


def generate_html(categories):

    os.makedirs("docs", exist_ok=True)

    total_count = sum(
        len(items)
        for items in categories.values()
    )

    html = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>오늘의 부동산 뉴스</title>

        <style>
            body{
                font-family: Arial, sans-serif;
                max-width: 1000px;
                margin: 30px auto;
                padding: 20px;
            }

            h1{
                color:#2c3e50;
            }

            .news-item{
                border-bottom:1px solid #ddd;
                padding:15px 0;
            }

            a{
                text-decoration:none;
                color:#0066cc;
            }

            a:hover{
                text-decoration:underline;
            }
        </style>
    </head>
    <body>

    <h1>🏢 오늘의 부동산 뉴스</h1>
    """
    html += f"""
    <div style="
        background:#f4f6f8;
        padding:15px;
        margin-bottom:20px;
        border-radius:10px;
    ">

    <b>총 기사수</b> : {total_count}<br>
    <b>송파구 뉴스</b> : {len(categories['송파구 뉴스'])}<br>
    <b>재건축 뉴스</b> : {len(categories['재건축 뉴스'])}<br>
    <b>상업용 부동산</b> : {len(categories['상업용 부동산'])}<br>
    <b>주택시장 뉴스</b> : {len(categories['주택시장 뉴스'])}

    </div>
    """

    for category_name, news_list in categories.items():

        html += f"""
        <h2>{category_name}</h2>
        """

        for idx, news in enumerate(news_list, start=1):
            html += f"""
            <div class="news-item">

                <h3>{idx}. {news['title']}</h3>

                <p>
                    {news.get('published', '')}
                </p>

                <a href="{news['link']}" target="_blank">
                    원문 보기
                </a>

            </div>
            """

    with open(
            "docs/index.html",
            "w",
            encoding="utf-8"
    ) as f:
        f.write(html)

    print("HTML 생성 완료")