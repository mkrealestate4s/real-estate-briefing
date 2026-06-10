from datetime import datetime


# ── 카테고리별 아이콘 / 색상 설정 ──────────────────────────
CATEGORY_CONFIG = {
    '송파구 뉴스':    {'icon': '📍', 'color': '#b45309', 'bg': '#fffbeb', 'border': '#fcd34d', 'tag_bg': '#fef3c7', 'tag_text': '#92400e'},
    '재건축 뉴스':   {'icon': '🏗️', 'color': '#1d4ed8', 'bg': '#eff6ff', 'border': '#93c5fd', 'tag_bg': '#dbeafe', 'tag_text': '#1e40af'},
    '상업용 부동산': {'icon': '🏢', 'color': '#0f766e', 'bg': '#f0fdfa', 'border': '#5eead4', 'tag_bg': '#ccfbf1', 'tag_text': '#134e4a'},
    '주택시장 뉴스': {'icon': '🏠', 'color': '#6d28d9', 'bg': '#faf5ff', 'border': '#c4b5fd', 'tag_bg': '#ede9fe', 'tag_text': '#4c1d95'},
}


def get_css() -> str:
    return """
    /* ── 리셋 & 기본 ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:       #f5f4f0;
      --surface:  #ffffff;
      --border:   #e5e3dc;
      --text-1:   #1c1917;
      --text-2:   #57534e;
      --text-3:   #a8a29e;
      --blue:     #1d4ed8;
      --radius-sm: 8px;
      --radius:    14px;
      --radius-lg: 20px;
      --shadow:    0 1px 4px rgba(0,0,0,.06), 0 4px 16px rgba(0,0,0,.06);
    }

    html { font-size: 16px; -webkit-text-size-adjust: 100%; }

    body {
      font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text-1);
      line-height: 1.65;
      min-height: 100vh;
    }

    /* ── 레이아웃 ── */
    .wrap { max-width: 900px; margin: 0 auto; padding: 24px 16px 60px; }

    /* ── 헤더 ── */
    .site-header {
      background: #0f172a;
      color: #f8fafc;
      border-radius: var(--radius-lg);
      padding: 28px 28px 24px;
      margin-bottom: 24px;
      position: relative;
      overflow: hidden;
    }
    .site-header::after {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(ellipse 60% 80% at 100% 0%, rgba(99,102,241,.25) 0%, transparent 70%);
      pointer-events: none;
    }
    .header-eyebrow {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: #94a3b8;
      margin-bottom: 8px;
    }
    .header-title {
      font-size: clamp(22px, 5vw, 32px);
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 16px;
    }
    .header-summary {
      font-size: 14px;
      color: #cbd5e1;
      background: rgba(255,255,255,.07);
      border: 1px solid rgba(255,255,255,.1);
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      line-height: 1.6;
    }

    /* ── 통계 카드 ── */
    .stats-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 12px;
      margin-bottom: 32px;
    }
    .stat-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      text-align: center;
    }
    .stat-card .stat-icon { font-size: 22px; display: block; margin-bottom: 4px; }
    .stat-card .stat-num  {
      font-size: clamp(26px, 6vw, 36px);
      font-weight: 700;
      line-height: 1;
      margin-bottom: 4px;
      color: var(--text-1);
    }
    .stat-card .stat-label {
      font-size: 12px;
      color: var(--text-2);
      font-weight: 500;
    }

    /* ── 섹션 헤더 ── */
    .section-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 36px 0 14px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--border);
    }
    .section-header .icon { font-size: 20px; }
    .section-header h2 {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-1);
    }
    .section-header .count {
      margin-left: auto;
      font-size: 12px;
      font-weight: 600;
      background: var(--bg);
      color: var(--text-2);
      padding: 3px 10px;
      border-radius: 20px;
      border: 1px solid var(--border);
    }

    /* ── 뉴스 카드 그리드 ── */
    .news-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 14px;
    }

    /* ── 뉴스 카드 ── */
    .news-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 18px 18px 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: box-shadow .18s, transform .18s;
      box-shadow: var(--shadow);
    }
    .news-card:hover {
      box-shadow: 0 4px 20px rgba(0,0,0,.1);
      transform: translateY(-2px);
    }

    .card-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .source-tag {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: .02em;
    }
    .date-tag {
      font-size: 11px;
      color: var(--text-3);
      margin-left: auto;
    }

    .card-title {
      font-size: 15px;
      font-weight: 700;
      line-height: 1.45;
      color: var(--text-1);
    }
    .card-summary {
      font-size: 13px;
      color: var(--text-2);
      line-height: 1.65;
      flex: 1;
    }

    .card-link {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      font-weight: 600;
      color: var(--blue);
      text-decoration: none;
      padding: 6px 0 2px;
      border-top: 1px solid var(--border);
      margin-top: auto;
    }
    .card-link:hover { text-decoration: underline; }
    .card-link::after { content: '↗'; font-size: 11px; }

    /* ── 푸터 ── */
    .site-footer {
      text-align: center;
      font-size: 12px;
      color: var(--text-3);
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
    }

    /* ── 모바일 ── */
    @media (max-width: 600px) {
      .wrap { padding: 16px 12px 48px; }
      .site-header { padding: 22px 18px 18px; border-radius: var(--radius); }
      .header-summary { font-size: 13px; }
      .stats-row { grid-template-columns: repeat(2, 1fr); }
      .news-grid { grid-template-columns: 1fr; }
      .section-header { margin-top: 28px; }
      .card-title { font-size: 14px; }
      .card-summary { font-size: 13px; }
    }

    @media (prefers-reduced-motion: reduce) {
      .news-card { transition: none; }
    }
    """


def build_stat_card(icon: str, number: int, label: str) -> str:
    return f"""
      <div class="stat-card">
        <span class="stat-icon">{icon}</span>
        <div class="stat-num">{number}</div>
        <div class="stat-label">{label}</div>
      </div>"""


def build_news_card(article: dict, category: str) -> str:
    cfg = CATEGORY_CONFIG.get(category, CATEGORY_CONFIG['주택시장 뉴스'])
    tag_style = f"background:{cfg['tag_bg']};color:{cfg['tag_text']};"
    source  = article.get('source', '')
    date    = article.get('date', '')[:10]
    title   = article.get('title', '')
    summary = article.get('summary', '')
    link    = article.get('link', '#')

    return f"""
      <div class="news-card">
        <div class="card-meta">
          <span class="source-tag" style="{tag_style}">{source}</span>
          <span class="date-tag">{date}</span>
        </div>
        <div class="card-title">{title}</div>
        <div class="card-summary">{summary}</div>
        <a class="card-link" href="{link}" target="_blank" rel="noopener">원문 보기</a>
      </div>"""


def build_section(category: str, articles: list) -> str:
    cfg = CATEGORY_CONFIG.get(category, CATEGORY_CONFIG['주택시장 뉴스'])
    icon  = cfg['icon']
    count = len(articles)

    cards = ''.join(build_news_card(a, category) for a in articles)

    return f"""
    <div class="section-header">
      <span class="icon">{icon}</span>
      <h2>{category}</h2>
      <span class="count">{count}건</span>
    </div>
    <div class="news-grid">{cards}
    </div>"""


def generate_html(
    total_count: int,
    categories: dict,           # { '카테고리명': [article, ...] }
    page_title: str = "오늘의 부동산 뉴스",
    one_line_summary: str = "",
    generated_at: str = "",
) -> str:
    """
    전체 HTML 문자열 반환.

    categories 형식:
    {
      '송파구 뉴스':    [{'title':..., 'source':..., 'date':..., 'link':..., 'summary':...}, ...],
      '재건축 뉴스':   [...],
      '상업용 부동산': [...],
      '주택시장 뉴스': [...],
    }
    """
    today = generated_at or datetime.now().strftime("%Y년 %m월 %d일")
    summary_text = one_line_summary or f"총 {total_count}건의 부동산 뉴스를 수집했습니다."

    # 통계 카드
    stats_html = (
        build_stat_card('📰', total_count, '전체 기사') +
        build_stat_card('📍', len(categories.get('송파구 뉴스', [])),    '송파구') +
        build_stat_card('🏗️', len(categories.get('재건축 뉴스', [])),   '재건축') +
        build_stat_card('🏢', len(categories.get('상업용 부동산', [])), '상업용') +
        build_stat_card('🏠', len(categories.get('주택시장 뉴스', [])), '주택시장')
    )

    # 섹션 순서: 송파 → 재건축 → 주택시장 → 상업용
    section_order = ['송파구 뉴스', '재건축 뉴스', '주택시장 뉴스', '상업용 부동산']
    sections_html = ''
    for cat in section_order:
        articles = categories.get(cat, [])
        if articles:
            sections_html += build_section(cat, articles)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta property="og:title" content="{today} 부동산 뉴스">
  <meta property="og:description" content="{summary_text}">
  <title>{page_title} — {today}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap">
  <style>{get_css()}
  </style>
</head>
<body>
<div class="wrap">

  <header class="site-header">
    <div class="header-eyebrow">{today} · 부동산 뉴스 브리핑</div>
    <h1 class="header-title">🏢 오늘의 부동산 뉴스</h1>
    <div class="header-summary">📌 {summary_text}</div>
  </header>

  <div class="stats-row">{stats_html}
  </div>

  {sections_html}

  <footer class="site-footer">
    자동 수집 · {today} 기준 &nbsp;|&nbsp; 본 페이지는 뉴스 링크 모음이며 투자 권유가 아닙니다
  </footer>

</div>
</body>
</html>"""


# ── 직접 실행 시 샘플 출력 ────────────────────────────────
if __name__ == "__main__":
    from briefing_html import total_count, categories, sample_articles

    html = generate_html(
        total_count=total_count,
        categories=sample_articles,
        one_line_summary="서울 분양가 21억 돌파 · 전셋값 545주 최고 · 잠실 재건축 기대감 재점화",
    )

    out = "/home/claude/briefing_preview.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 생성 완료: {out}  ({len(html):,} bytes)")
