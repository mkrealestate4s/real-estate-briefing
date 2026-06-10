def classify_news(news_list):

    categories = {
        "송파구 뉴스": [],
        "재건축 뉴스": [],
        "금융·정책 뉴스": [],
        "상업용 부동산": [],
        "주택시장 뉴스": [],
        "기타 뉴스": []
    }

    for news in news_list:

        title = news.get("title", "") + " " + news.get("summary", "")

        if any(keyword in title for keyword in [
            "송파", "잠실", "문정", "가락", "석촌", "삼전", "방이",
            "신천", "풍납", "거여", "마천", "오금", "장지", "위례",
            "헬리오시티", "파크리오", "리센츠", "엘스", "트리지움",
            "잠실주공", "잠실우성", "가락시영"
        ]):
            categories["송파구 뉴스"].append(news)

        elif any(keyword in title for keyword in [
            "재건축", "재개발", "정비사업", "신통기획", "안전진단",
            "조합설립", "사업시행인가", "관리처분", "이주", "철거",
            "준공", "착공", "시공사", "조합원", "분담금",
            "용적률", "층수", "세대수", "신축", "리모델링"
        ]):
            categories["재건축 뉴스"].append(news)

        elif any(keyword in title for keyword in [
            "금리", "기준금리", "DSR", "LTV", "DTI",
            "대출", "담보대출", "주담대", "전세대출",
            "규제", "완화", "강화", "정책", "대책",
            "양도세", "취득세", "종부세", "보유세", "세금",
            "장기보유", "비과세", "공시가격", "국토부",
            "한국은행", "금융위", "금감원"
        ]):
            categories["금융·정책 뉴스"].append(news)

        elif any(keyword in title for keyword in [
            "오피스", "오피스텔", "상가", "빌딩", "지식산업센터",
            "공실", "임대료", "임대차", "꼬마빌딩", "수익형",
            "GBD", "CBD", "YBD", "강남업무", "도심",
            "리테일", "물류", "데이터센터", "호텔"
        ]):
            categories["상업용 부동산"].append(news)

        elif any(keyword in title for keyword in [
            "아파트", "전세", "분양", "주택", "청약", "미분양",
            "매매", "전셋값", "집값", "부동산", "실거래",
            "공급", "입주", "준공", "착공", "인허가",
            "경매", "낙찰", "강남", "서초", "용산",
            "갭투자", "투자", "매물", "호가", "신고가"
        ]):
            categories["주택시장 뉴스"].append(news)

        else:
            categories["기타 뉴스"].append(news)

    return categories