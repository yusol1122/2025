import streamlit as st

st.set_page_config(page_title="문화 취향 나라 추천기", page_icon="🌍", layout="centered")

st.title("🌍 문화 취향 기반 나라 추천기")
st.write("몇 가지 간단한 질문에 답하고, 당신과 어울리는 나라를 찾아보세요!")

# 질문 1
food = st.radio("🍜 어떤 음식을 더 좋아하나요?", 
                ["매운 음식", "달콤한 음식", "담백한 음식", "향신료 강한 음식"])

# 질문 2
music = st.radio("🎶 어떤 음악을 더 즐기나요?", 
                 ["K-Pop/댄스", "클래식/재즈", "EDM/힙합", "전통 음악"])

# 질문 3
climate = st.radio("☀️ 어떤 기후를 선호하시나요?", 
                   ["따뜻하고 습한 곳", "선선하고 온화한 곳", "추운 곳", "건조하고 뜨거운 곳"])

# 질문 4
travel = st.radio("🗺️ 여행 스타일은?", 
                  ["도시 탐험", "자연 힐링", "역사와 문화 탐방", "바다와 휴양"])

# 추천 로직
if st.button("추천받기 🚀"):
    score = {"한국":0, "일본":0, "이탈리아":0, "브라질":0, "이집트":0}

    # 음식 매칭
    if food == "매운 음식": score["한국"] += 1; score["브라질"] += 1
    elif food == "달콤한 음식": score["이탈리아"] += 1
    elif food == "담백한 음식": score["일본"] += 1
    elif food == "향신료 강한 음식": score["이집트"] += 1

    # 음악 매칭
    if music == "K-Pop/댄스": score["한국"] += 1
    elif music == "클래식/재즈": score["이탈리아"] += 1
    elif music == "EDM/힙합": score["브라질"] += 1
    elif music == "전통 음악": score["일본"] += 1; score["이집트"] += 1

    # 기후 매칭
    if climate == "따뜻하고 습한 곳": score["브라질"] += 1
    elif climate == "선선하고 온화한 곳": score["이탈리아"] += 1; score["일본"] += 1
    elif climate == "추운 곳": score["한국"] += 1
    elif climate == "건조하고 뜨거운 곳": score["이집트"] += 1

    # 여행 스타일 매칭
    if travel == "도시 탐험": score["한국"] += 1; score["이탈리아"] += 1
    elif travel == "자연 힐링": score["브라질"] += 1; score["일본"] += 1
    elif travel == "역사와 문화 탐방": score["이탈리아"] += 1; score["이집트"] += 1
    elif travel == "바다와 휴양": score["브라질"] += 1; score["이집트"] += 1

    # 최고 점수 나라
    best_country = max(score, key=score.get)

    st.subheader(f"✨ 당신과 어울리는 나라는 바로... **{best_country}** 🇨🇭")
    
    descriptions = {
        "한국": "🔥 열정적이고 다채로운 현대 문화와 전통이 공존하는 나라! K-Pop, 맛있는 매운 음식, 역동적인 도시가 기다립니다.",
        "일본": "🎌 정갈하고 세련된 문화, 애니메이션과 전통이 어우러진 매력적인 나라. 온천과 벚꽃 여행도 필수!",
        "이탈리아": "🍕 파스타, 피자, 와인과 함께하는 낭만! 미술, 건축, 패션까지 즐길 수 있는 문화의 중심지.",
        "브라질": "🎉 삼바와 축구, 카니발의 나라! 활기찬 사람들과 열대 우림, 해변이 기다립니다.",
        "이집트": "🏺 피라미드와 스핑크스, 고대 문명의 발자취가 남아있는 곳. 이국적이고 신비로운 여행지!"
    }
    
    st.write(descriptions[best_country])

