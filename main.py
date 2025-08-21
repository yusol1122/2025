import streamlit as st

# MBTI별 추천 직업 데이터
career_dict = {
    "ISTJ": ["회계사", "법률가", "군인", "행정 공무원"],
    "ISFJ": ["간호사", "교사", "사회복지사", "비서"],
    "INFJ": ["상담가", "작가", "심리학자", "교육자"],
    "INTJ": ["전략 컨설턴트", "데이터 사이언티스트", "연구원", "엔지니어"],

    "ISTP": ["엔지니어", "파일럿", "응급구조사", "기술자"],
    "ISFP": ["예술가", "디자이너", "치료사", "사진작가"],
    "INFP": ["작가", "상담사", "교사", "심리학자"],
    "INTP": ["연구원", "프로그래머", "발명가", "데이터 분석가"],

    "ESTP": ["기업가", "영업 전문가", "스포츠 선수", "소방관"],
    "ESFP": ["배우", "이벤트 기획자", "홍보 전문가", "가수"],
    "ENFP": ["마케터", "언론인", "강연가", "창업가"],
    "ENTP": ["기업가", "크리에이티브 디렉터", "변호사", "발명가"],

    "ESTJ": ["경영자", "군 장교", "프로젝트 매니저", "행정가"],
    "ESFJ": ["교사", "의료 전문가", "상담사", "사회복지사"],
    "ENFJ": ["지도자", "교육자", "정치인", "인사 담당자"],
    "ENTJ": ["CEO", "전략 기획가", "변호사", "경영 컨설턴트"]
}

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟")

st.title("🌟 MBTI 기반 진로 추천 웹앱")
st.write("자신의 MBTI를 선택하면 추천 직업을 알려드립니다!")

# MBTI 선택
mbti_list = list(career_dict.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형 추천 직업")
    for job in career_dict[selected_mbti]:
        st.write(f"- {job}")

