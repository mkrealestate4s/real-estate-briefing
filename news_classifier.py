def classify_news(news_list):

    categories = {
        "송파구 뉴스": [],
        "재건축 뉴스": [],
        "상업용 부동산": [],
        "주택시장 뉴스": [],
        "기타 뉴스": []
    }

    for news in news_list:

        title = news["title"]

        if any(keyword in title for keyword in [
            "송파", "잠실", "문정", "가락",
            "석촌", "삼전", "방이"
        ]):
            categories["송파구 뉴스"].append(news)

        elif any(keyword in title for keyword in [
            "재건축", "재개발", "정비사업",
            "신통기획", "안전진단"
        ]):
            categories["재건축 뉴스"].append(news)

        elif any(keyword in title for keyword in [
            "오피스", "오피스텔", "상가",
            "빌딩", "지식산업센터",
            "공실", "임대료"
        ]):
            categories["상업용 부동산"].append(news)

        elif any(keyword in title for keyword in [
            "아파트", "전세", "분양",
            "주택", "청약", "미분양"
        ]):
            categories["주택시장 뉴스"].append(news)

        else:
            categories["기타 뉴스"].append(news)

    return categories