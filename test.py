import streamlit as st

st.set_page_config(page_title="문화 취향 나라 추천기", page_icon="🌍", layout="centered")

st.title("🌍 문화 취향 기반 나라 추천기")
st.markdown("✨ 몇 가지 질문에 답하고, 당신과 꼭 맞는 나라 TOP 3를 찾아보세요! ✨")

# ---------------- 질문 카드 ---------------- #
with st.container():
    st.markdown("### 🍜 음식 취향")
    food = st.radio("당신의 음식 스타일은?", 
                    ["매운 음식 🌶️🔥", "달콤한 음식 🍰🍯", "담백한 음식 🥗🍵", "고기 위주 음식 🥩🍖", "향신료 강한 음식 🍛🌿"], 
                    horizontal=True)

with st.container():
    st.markdown("### 🎶 음악 취향")
    music = st.radio("당신이 즐겨 듣는 음악은?", 
                     ["팝/댄스 🎤💃", "클래식/재즈 🎻🎷", "전통 음악 🥁🪕", "축제/리듬 강한 음악 🎉🥳"], 
                     horizontal=True)

with st.container():
    st.markdown("### ☀️ 기후 선호")
    climate = st.radio("어떤 기후를 선호하시나요?", 
                       ["사계절 뚜렷한 곳 🍂❄️🌸☀️", "따뜻하고 습한 곳 🌴☀️", "선선하고 온화한 곳 🌤️🍃", "추운 곳 ❄️🥶", "건조하고 뜨거운 곳 🏜️🔥"], 
                       horizontal=True)

with st.container():
    st.markdown("### 🏨 숙소 스타일")
    stay = st.radio("여행할 때 선호하는 숙소는?", 
                    ["럭셔리 호텔 🏰✨", "게스트하우스/에어비앤비 🏡🛏️", "자연 속 리조트/방갈로 🌺🌊", "캠핑/야생 숙소 ⛺🔥"], 
                    horizontal=True)

with st.container():
    st.markdown("### 🥂 여행 중 즐기는 활동")
    activity = st.radio("여행할 때 나는...", 
                        ["미식 여행 🍝🍷", "쇼핑 🛍️💎", "축제·파티 🎊🎶", "힐링·자연 🌲🧘", "모험·스포츠 🧗🏄"], 
                        horizontal=True)

# ---------------- 버튼 ---------------- #
if st.button("추천받기 🚀"):
    # 국가별 점수 초기화
    countries = {
        # 아시아
        "한국 🇰🇷":0, "일본 🇯🇵":0, "인도 🇮🇳":0, "태국 🇹🇭":0, "중국 🇨🇳":0, "사우디아라비아 🇸🇦":0, "터키 🇹🇷":0,
        # 유럽
        "프랑스 🇫🇷":0, "이탈리아 🇮🇹":0, "스페인 🇪🇸":0,
        "스웨덴 🇸🇪":0, "노르웨이 🇳🇴":0, "핀란드 🇫🇮":0,
        "폴란드 🇵🇱":0, "체코 🇨🇿":0, "러시아 🇷🇺":0,
        # 아메리카
        "미국 🇺🇸":0, "캐나다 🇨🇦":0, "멕시코 🇲🇽":0,
        "브라질 🇧🇷":0, "아르헨티나 🇦🇷":0, "칠레 🇨🇱":0, "페루 🇵🇪":0,
        # 아프리카
        "이집트 🇪🇬":0, "남아공 🇿🇦":0, "모로코 🇲🇦":0, "케냐 🇰🇪":0,
        # 오세아니아
        "호주 🇦🇺":0, "뉴질랜드 🇳🇿":0, "피지 🇫🇯":0
    }

    # 음식 매핑
    if food.startswith("매운"):
        for c in ["한국 🇰🇷","태국 🇹🇭","멕시코 🇲🇽","중국 🇨🇳"]: countries[c]+=1
    elif food.startswith("달콤"):
        for c in ["프랑스 🇫🇷","이탈리아 🇮🇹","미국 🇺🇸"]: countries[c]+=1
    elif food.startswith("담백"):
        for c in ["일본 🇯🇵","스웨덴 🇸🇪","핀란드 🇫🇮"]: countries[c]+=1
    elif food.startswith("고기"):
        for c in ["아르헨티나 🇦🇷","호주 🇦🇺","브라질 🇧🇷"]: countries[c]+=1
    elif food.startswith("향신료"):
        for c in ["인도 🇮🇳","모로코 🇲🇦","이집트 🇪🇬","사우디아라비아 🇸🇦","터키 🇹🇷"]: countries[c]+=1

    # 음악 매핑
    if music.startswith("팝"):
        for c in ["한국 🇰🇷","미국 🇺🇸","프랑스 🇫🇷"]: countries[c]+=1
    elif music.startswith("클래식"):
        for c in ["프랑스 🇫🇷","이탈리아 🇮🇹","러시아 🇷🇺"]: countries[c]+=1
    elif music.startswith("전통"):
        for c in ["일본 🇯🇵","인도 🇮🇳","케냐 🇰🇪","사우디아라비아 🇸🇦","터키 🇹🇷","중국 🇨🇳"]: countries[c]+=1
    elif music.startswith("축제"):
        for c in ["브라질 🇧🇷","스페인 🇪🇸","멕시코 🇲🇽","남아공 🇿🇦"]: countries[c]+=1

    # 기후 매핑
    if climate.startswith("사계절"):
        for c in ["한국 🇰🇷","미국 🇺🇸","캐나다 🇨🇦","폴란드 🇵🇱"]: countries[c]+=1
    elif climate.startswith("따뜻"):
        for c in ["태국 🇹🇭","브라질 🇧🇷","인도 🇮🇳","피지 🇫🇯"]: countries[c]+=1
    elif climate.startswith("선선"):
        for c in ["프랑스 🇫🇷","스페인 🇪🇸","칠레 🇨🇱","뉴질랜드 🇳🇿"]: countries[c]+=1
    elif climate.startswith("추운"):
        for c in ["캐나다 🇨🇦","러시아 🇷🇺","핀란드 🇫🇮","노르웨이 🇳🇴"]: countries[c]+=1
    elif climate.startswith("건조"):
        for c in ["이집트 🇪🇬","모로코 🇲🇦","사우디아라비아 🇸🇦","케냐 🇰🇪"]: countries[c]+=1

    # 숙소 매핑
    if stay.startswith("럭셔리"):
        for c in ["미국 🇺🇸","프랑스 🇫🇷","한국 🇰🇷","사우디아라비아 🇸🇦"]: countries[c]+=1
    elif stay.startswith("게스트"):
        for c in ["일본 🇯🇵","체코 🇨🇿","스페인 🇪🇸","멕시코 🇲🇽"]: countries[c]+=1
    elif stay.startswith("자연"):
        for c in ["태국 🇹🇭","피지 🇫🇯","뉴질랜드 🇳🇿","케냐 🇰🇪"]: countries[c]+=1
    elif stay.startswith("캠핑"):
        for c in ["캐나다 🇨🇦","핀란드 🇫🇮","남아공 🇿🇦","칠레 🇨🇱"]: countries[c]+=1

    # 여행 활동 매핑
    if activity.startswith("미식"):
        for c in ["이탈리아 🇮🇹","프랑스 🇫🇷","태국 🇹🇭","멕시코 🇲🇽"]: countries[c]+=1
    elif activity.startswith("쇼핑"):
        for c in ["한국 🇰🇷","일본 🇯🇵","미국 🇺🇸","중국 🇨🇳"]: countries[c]+=1
    elif activity.startswith("축제"):
        for c in ["스페인 🇪🇸","브라질 🇧🇷","멕시코 🇲🇽","남아공 🇿🇦"]: countries[c]+=1
    elif activity.startswith("힐링"):
        for c in ["뉴질랜드 🇳🇿","캐나다 🇨🇦","핀란드 🇫🇮","케냐 🇰🇪"]: countries[c]+=1
    elif activity.startswith("모험"):
        for c in ["호주 🇦🇺","칠레 🇨🇱","남아공 🇿🇦","노르웨이 🇳🇴"]: countries[c]+=1

    # ---------------- 결과 계산 ---------------- #
    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_countries[:3]

    descriptions = {
        "한국 🇰🇷":"🔥 K-pop, 한식, 전통과 현대가 공존하는 나라 🎶🍜🏙️",
        "일본 🇯🇵":"🎌 애니메이션, 온천, 사쿠라까지 다채로운 매력 🍣🌸🏯",
        "인도 🇮🇳":"🕌 향신료, 요가, 다채로운 색의 나라 🌈🍛🪔",
        "태국 🇹🇭":"🌴 미소의 나라, 맛있는 음식과 휴양 천국 😋🍹🏖️",
        "중국 🇨🇳":"🐉 거대한 역사와 다양한 음식, 문화의 용 🏯🥟🚄",
        "사우디아라비아 🇸🇦":"⛽ 사막, 오아시스, 이슬람 문화의 중심 🏜️🕌",
        "터키 🇹🇷":"🕌 유럽과 아시아의 다리, 미식과 역사 🌉🥙",
        "프랑스 🇫🇷":"🍷 낭만과 예술, 와인의 천국 🗼🥖🎨",
        "이탈리아 🇮🇹":"🍕 르네상스와 파스타, 로마의 유산 🍝🏛️",
        "스페인 🇪🇸":"💃 태양과 플라멩코, 지중해의 낭만 🌞🍷",
        "스웨덴 🇸🇪":"❄️ 북유럽 감성, 디자인과 자연의 조화 🛶🏔️",
        "노르웨이 🇳🇴":"🏔️ 피오르드와 오로라의 나라 🌌🛳️",
        "핀란드 🇫🇮":"🦌 산타마을과 청정 자연의 고향 🎅🌲",
        "폴란드 🇵🇱":"🏰 중세 도시와 근현대 역사 🏙️⚔️",
        "체코 🇨🇿":"🍺 프라하와 맥주의 천국 🏰🍻",
        "러시아 🇷🇺":"❄️ 끝없는 대지와 예술의 나라 🎭🖼️",
        "미국 🇺🇸":"🎬 자유와 기회의 땅, 헐리우드와 대도시 🗽🍔",
        "캐나다 🇨🇦":"🍁 광활한 자연과 다문화 사회 🦌🏞️",
        "멕시코 🇲🇽":"🌮 타코와 마야·아즈텍 문명 🎶🌵",
        "브라질 🇧🇷":"🎉 삼바, 카니발, 아마존 정글 🥁🌳",
        "아르헨티나 🇦🇷":"🥩 탱고와 스테이크, 열정의 나라 💃🍷",
        "칠레 🇨🇱":"🌋 안데스와 와인의 나라 🍇🏔️",
        "페루 🇵🇪":"🏔️ 마추픽추와 잉카 문명 🦙🌄",
        "이집트 🇪🇬":"🏺 피라미드와 스핑크스, 고대 신비 🐪🌞",
        "남아공 🇿🇦":"🦁 사파리와 다양한 문화 🌍🎶",
        "모로코 🇲🇦":"🌙 아랍 시장과 사하라의 매력 🕌🐪",
        "케냐 🇰🇪":"🐘 야생 사파리와 대자연 🦒🌳",
        "호주 🇦🇺":"🐨 대자연과 현대 도시 🌊🏙️",
        "뉴질랜드 🇳🇿":"⛰️ 반지의 제왕 촬영지, 청정 자연 🏞️🐑",
        "피지 🇫🇯":"🏝️ 남태평양의 천국 🌊🍹",
    }

    # ---------------- 결과 카드 ---------------- #
    st.subheader("🌟 당신과 어울리는 TOP 3 나라 🌟")
    for i, (country, score) in enumerate(top3, start=1):
        desc = descriptions.get(country, "매력적인 나라예요! 🎉🌍✨")
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
                        border-radius:20px; padding:25px; margin-bottom:20px; 
                        box-shadow:4px 4px 15px rgba(0,0,0,0.2);">
                <h2 style="text-align:center; font-size:40px;">🥇 TOP {i}: {country} 🌈✨</h2>
                <p style="text-align:center; font-size:22px;">{desc} 🎉🎶🌍💃🦁✨</p>
            </div>
            """,
            unsafe_allow_html=True
        )
