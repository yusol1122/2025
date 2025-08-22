import streamlit as st

st.set_page_config(page_title="문화 취향 나라 추천기", page_icon="🌍", layout="centered")

st.title("🌍 문화 취향 기반 나라 추천기")
st.markdown("✨ 몇 가지 질문에 답하고, 당신과 꼭 맞는 나라 TOP 3를 찾아보세요! ✨")

# ---------------- 질문 카드 ---------------- #
with st.container():
    st.markdown("### 🍜 음식 취향")
    food = st.radio("당신의 음식 스타일은?", 
                    ["매운 음식", "달콤한 음식", "담백한 음식", "고기 위주 음식", "향신료 강한 음식"], 
                    horizontal=True)

with st.container():
    st.markdown("### 🎶 음악 취향")
    music = st.radio("당신이 즐겨 듣는 음악은?", 
                     ["팝/댄스", "클래식/재즈", "전통 음악", "축제/리듬 강한 음악"], 
                     horizontal=True)

with st.container():
    st.markdown("### ☀️ 기후 선호")
    climate = st.radio("어떤 기후를 선호하시나요?", 
                       ["사계절 뚜렷한 곳", "따뜻하고 습한 곳", "선선하고 온화한 곳", "추운 곳", "건조하고 뜨거운 곳"], 
                       horizontal=True)

with st.container():
    st.markdown("### 🏨 숙소 스타일")
    stay = st.radio("여행할 때 선호하는 숙소는?", 
                    ["럭셔리 호텔", "게스트하우스/에어비앤비", "자연 속 리조트/방갈로", "캠핑/야생 숙소"], 
                    horizontal=True)

with st.container():
    st.markdown("### 🥂 여행 중 즐기는 활동")
    activity = st.radio("여행할 때 나는...", 
                        ["미식 여행", "쇼핑", "축제·파티", "힐링·자연", "모험·스포츠"], 
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
    if food == "매운 음식":
        for c in ["한국 🇰🇷","태국 🇹🇭","멕시코 🇲🇽","중국 🇨🇳"]: countries[c]+=1
    elif food == "달콤한 음식":
        for c in ["프랑스 🇫🇷","이탈리아 🇮🇹","미국 🇺🇸"]: countries[c]+=1
    elif food == "담백한 음식":
        for c in ["일본 🇯🇵","스웨덴 🇸🇪","핀란드 🇫🇮"]: countries[c]+=1
    elif food == "고기 위주 음식":
        for c in ["아르헨티나 🇦🇷","호주 🇦🇺","브라질 🇧🇷"]: countries[c]+=1
    elif food == "향신료 강한 음식":
        for c in ["인도 🇮🇳","모로코 🇲🇦","이집트 🇪🇬","사우디아라비아 🇸🇦","터키 🇹🇷"]: countries[c]+=1

    # 음악 매핑
    if music == "팝/댄스":
        for c in ["한국 🇰🇷","미국 🇺🇸","프랑스 🇫🇷"]: countries[c]+=1
    elif music == "클래식/재즈":
        for c in ["프랑스 🇫🇷","이탈리아 🇮🇹","러시아 🇷🇺"]: countries[c]+=1
    elif music == "전통 음악":
        for c in ["일본 🇯🇵","인도 🇮🇳","케냐 🇰🇪","사우디아라비아 🇸🇦","터키 🇹🇷","중국 🇨🇳"]: countries[c]+=1
    elif music == "축제/리듬 강한 음악":
        for c in ["브라질 🇧🇷","스페인 🇪🇸","멕시코 🇲🇽","남아공 🇿🇦"]: countries[c]+=1

    # 기후 매핑
    if climate == "사계절 뚜렷한 곳":
        for c in ["한국 🇰🇷","미국 🇺🇸","캐나다 🇨🇦","폴란드 🇵🇱"]: countries[c]+=1
    elif climate == "따뜻하고 습한 곳":
        for c in ["태국 🇹🇭","브라질 🇧🇷","인도 🇮🇳","피지 🇫🇯"]: countries[c]+=1
    elif climate == "선선하고 온화한 곳":
        for c in ["프랑스 🇫🇷","스페인 🇪🇸","칠레 🇨🇱","뉴질랜드 🇳🇿"]: countries[c]+=1
    elif climate == "추운 곳":
        for c in ["캐나다 🇨🇦","러시아 🇷🇺","핀란드 🇫🇮","노르웨이 🇳🇴"]: countries[c]+=1
    elif climate == "건조하고 뜨거운 곳":
        for c in ["이집트 🇪🇬","모로코 🇲🇦","사우디아라비아 🇸🇦","케냐 🇰🇪"]: countries[c]+=1

    # 숙소 매핑
    if stay == "럭셔리 호텔":
        for c in ["미국 🇺🇸","프랑스 🇫🇷","한국 🇰🇷","사우디아라비아 🇸🇦"]: countries[c]+=1
    elif stay == "게스트하우스/에어비앤비":
        for c in ["일본 🇯🇵","체코 🇨🇿","스페인 🇪🇸","멕시코 🇲🇽"]: countries[c]+=1
    elif stay == "자연 속 리조트/방갈로":
        for c in ["태국 🇹🇭","피지 🇫🇯","뉴질랜드 🇳🇿","케냐 🇰🇪"]: countries[c]+=1
    elif stay == "캠핑/야생 숙소":
        for c in ["캐나다 🇨🇦","핀란드 🇫🇮","남아공 🇿🇦","칠레 🇨🇱"]: countries[c]+=1

    # 여행 중 활동 매핑
    if activity == "미식 여행":
        for c in ["이탈리아 🇮🇹","프랑스 🇫🇷","태국 🇹🇭","멕시코 🇲🇽"]: countries[c]+=1
    elif activity == "쇼핑":
        for c in ["한국 🇰🇷","일본 🇯🇵","미국 🇺🇸","중국 🇨🇳"]: countries[c]+=1
    elif activity == "축제·파티":
        for c in ["스페인 🇪🇸","브라질 🇧🇷","멕시코 🇲🇽","남아공 🇿🇦"]: countries[c]+=1
    elif activity == "힐링·자연":
        for c in ["뉴질랜드 🇳🇿","캐나다 🇨🇦","핀란드 🇫🇮","케냐 🇰🇪"]: countries[c]+=1
    elif activity == "모험·스포츠":
        for c in ["호주 🇦🇺","칠레 🇨🇱","남아공 🇿🇦","노르웨이 🇳🇴"]: countries[c]+=1

    # ---------------- 결과 계산 ---------------- #
    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_countries[:3]

    descriptions = {
        "한국 🇰🇷":"🔥 K-pop과 IT, 전통과 현대가 공존하는 역동적인 나라!",
        "일본 🇯🇵":"🎌 애니메이션, 온천, 전통과 첨단이 만나는 곳!",
        "인도 🇮🇳":"🕌 향신료와 다채로운 종교·문화가 공존하는 신비로운 나라!",
        "태국 🇹🇭":"🌴 미소의 나라, 맛있는 길거리 음식과 열대 휴양지!",
        "중국 🇨🇳":"🐉 거대한 역사와 다양한 음식, 세계적 문화 중심지!",
        "사우디아라비아 🇸🇦":"⛽ 사막과 오아시스, 이슬람 문화의 중심지!",
        "터키 🇹🇷":"🕌 유럽과 아시아의 경계, 역사와 미식의 나라!",
        "프랑스 🇫🇷":"🍷 예술, 와인, 낭만의 도시 파리!",
        "이탈리아 🇮🇹":"🍕 파스타, 르네상스 예술, 로마의 유산!",
        "스페인 🇪🇸":"💃 플라멩코, 태양, 지중해의 낭만!",
        "스웨덴 🇸🇪":"❄️ 북유럽 감성, 디자인과 자연의 조화!",
        "노르웨이 🇳🇴":"🏔️ 피오르드와 오로라의 나라!",
        "핀란드 🇫🇮":"🦌 산타 마을과 청정 자연의 고향!",
        "폴란드 🇵🇱":"🏰 중세 도시와 근현대 역사가 어우러진 나라!",
        "체코 🇨🇿":"🍺 맥주와 중세 건축의 천국, 프라하!",
        "러시아 🇷🇺":"❄️ 끝없는 대지와 예술·문학의 나라!",
        "미국 🇺🇸":"🎬 자유와 기회의 땅, 헐리우드와 대도시!",
        "캐나다 🇨🇦":"🍁 광활한 자연과 다문화 사회!",
        "멕시코 🇲🇽":"🌮 타코와 마야·아즈텍 문명!",
        "브라질 🇧🇷":"🎉 삼바, 카니발, 아마존 정글!",
        "아르헨티나 🇦🇷":"🥩 탱고와 스테이크, 자연과 도시가 어우러진 나라!",
        "칠레 🇨🇱":"🌋 안데스와 와인의 나라!",
        "페루 🇵🇪":"🏔️ 마추픽추와 잉카 문명의 흔적!",
        "이집트 🇪🇬":"🏺 피라미드와 스핑크스, 고대 문명의 신비!",
        "남아공 🇿🇦":"🦁 사파리와 다양한 인종·문화가 공존하는 곳!",
        "모로코 🇲🇦":"🌙 아랍 시장과 사하라 사막!",
        "케냐 🇰🇪":"🐘 야생 사파리와 대자연!",
        "호주 🇦🇺":"🐨 대자연과 현대 도시가 공존하는 나라!",
        "뉴질랜드 🇳🇿":"⛰️ 반지의 제왕 촬영지, 청정 자연의 천국!",
        "피지 🇫🇯":"🏝️ 남태평양의 휴양지, 천국 같은 바다!"
    }

    images = {
        "한국 🇰🇷":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Seoul_skyline.jpg/640px-Seoul_skyline.jpg",
        "일본 🇯🇵":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mount_Fuji_from_Hotel_Mt_Fuji_1995-3-20.jpg/640px-Mount_Fuji_from_Hotel_Mt_Fuji_1995-3-20.jpg",
        "인도 🇮🇳":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Taj-Mahal.jpg/640px-Taj-Mahal.jpg",
        "태국 🇹🇭":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Wat_Phra_Kaew_Bangkok.jpg/640px-Wat_Phra_Kaew_Bangkok.jpg",
        "중국 🇨🇳":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/GreatWall_2018.jpg/640px-GreatWall_2018.jpg",
        "사우디아라비아 🇸🇦":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Kaaba_Mecca.jpg/640px-Kaaba_Mecca.jpg",
        "터키 🇹🇷":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Hagia_Sophia_Mars_2013.jpg/640px-Hagia_Sophia_Mars_2013.jpg",
        "프랑스 🇫🇷":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg/640px-Tour_Eiffel_Wikimedia_Commons.jpg",
        "이탈리아 🇮🇹":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Colosseum_in_Rome%2C_Italy_-_April_2007.jpg/640px-Colosseum_in_Rome%2C_Italy_-_April_2007.jpg",
        "스페인 🇪🇸":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Sagrada_Familia_01.jpg/640px-Sagrada_Familia_01.jpg",
        "스웨덴 🇸🇪":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Stockholm_city.jpg/640px-Stockholm_city.jpg",
        "노르웨이 🇳🇴":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Geirangerfjord_from_flydalsjuvet.jpg/640px-Geirangerfjord_from_flydalsjuvet.jpg",
        "핀란드 🇫🇮":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Helsinki_cathedral.jpg/640px-Helsinki_cathedral.jpg",
        "폴란드 🇵🇱":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Wawel_Castle_05.jpg/640px-Wawel_Castle_05.jpg",
        "체코 🇨🇿":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Prague_Castle_and_Charles_Bridge.jpg/640px-Prague_Castle_and_Charles_Bridge.jpg",
        "러시아 🇷🇺":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Moscow_July_2011-7a.jpg/640px-Moscow_July_2011-7a.jpg",
        "미국 🇺🇸":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/New_York_City_skyline.jpg/640px-New_York_City_skyline.jpg",
        "캐나다 🇨🇦":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Niagara_Falls_2.jpg/640px-Niagara_Falls_2.jpg",
        "멕시코 🇲🇽":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Chichen_Itza_3.jpg/640px-Chichen_Itza_3.jpg",
        "브라질 🇧🇷":"https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Rio_de_Janeiro_Christ_the_Redeemer.jpg/640px-Rio_de_Janeiro_Christ_the_Redeemer.jpg",
        "아르헨티나 🇦🇷":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Buenos_Aires%2C_Congreso_de_la_Naci%C3%B3n_Argentina.jpg/640px-Buenos_Aires%2C_Congreso_de_la_Naci%C3%B3n_Argentina.jpg",
        "칠레 🇨🇱":"https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Torres_del_Paine.jpg/640px-Torres_del_Paine.jpg",
        "페루 🇵🇪":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Machu_Picchu%2C_Peru.jpg/640px-Machu_Picchu%2C_Peru.jpg",
        "이집트 🇪🇬":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/All_Gizah_Pyramids.jpg/640px-All_Gizah_Pyramids.jpg",
        "남아공 🇿🇦":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Cape_Town_and_Table_Mountain.jpg/640px-Cape_Town_and_Table_Mountain.jpg",
        "모로코 🇲🇦":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Casablanca_Morocco.jpg/640px-Casablanca_Morocco.jpg",
        "케냐 🇰🇪":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Masai_Mara_Kenya.jpg/640px-Masai_Mara_Kenya.jpg",
        "호주 🇦🇺":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Sydney_Opera_House_Sails.jpg/640px-Sydney_Opera_House_Sails.jpg",
        "뉴질랜드 🇳🇿":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Milford_Sound_NZ.jpg/640px-Milford_Sound_NZ.jpg",
        "피지 🇫🇯":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Fiji_beach.jpg/640px-Fiji_beach.jpg",
    }

    st.subheader("🌟 당신과 어울리는 TOP 3 나라 🌟")
    for i, (country, score) in enumerate(top3, start=1):
        st.markdown(f"## 🥇 TOP {i}: {country}")
        st.write(descriptions.get(country, "매력적인 나라예요!"))
        if country in images:
            st.image(images[country], use_column_width=True)
