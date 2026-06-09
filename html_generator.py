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
                    font-family: "Segoe UI", sans-serif;
                    background:#f4f6f8;
                    margin:0;
                    padding:30px;
                }
                
                .container{
                    max-width:1200px;
                    margin:auto;
                }
                
                h1{
                    color:#1f2937;
                    margin-bottom:10px;
                }
                
                h2{
                    margin-top:40px;
                    color:#374151;
                }
                
                .dashboard{
                    display:flex;
                    gap:15px;
                    margin-bottom:30px;
                    flex-wrap:wrap;
                }
                
                .stat-card{
                    background:white;
                    padding:20px;
                    border-radius:12px;
                    box-shadow:0 2px 10px rgba(0,0,0,0.08);
                    flex:1;
                    min-width:180px;
                    text-align:center;
                }
                
                .stat-card .number{
                    font-size:32px;
                    font-weight:bold;
                    margin-top:10px;
                }
                
                .news-grid{
                    display:grid;
                    grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
                    gap:20px;
                }
                
                .news-item{
                    background:white;
                    padding:20px;
                    border-radius:12px;
                    box-shadow:0 2px 8px rgba(0,0,0,0.08);
                    transition:0.2s;
                }
                
                .news-item:hover{
                    transform:translateY(-3px);
                }
                
                .news-item h3{
                    font-size:18px;
                    line-height:1.4;
                }
                
                .news-item a{
                    display:inline-block;
                    margin-top:10px;
                    color:#2563eb;
                    font-weight:bold;
                    text-decoration:none;
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
    output_path = os.path.abspath("docs/index.html")

    print("저장 위치:", output_path)


    with open(
            "docs/index.html",
            "w",
            encoding="utf-8"
    ) as f:
        f.write(html)

    print("HTML 생성 완료")