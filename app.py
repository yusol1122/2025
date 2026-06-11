import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="디지털 성범죄 예방 교육",
    page_icon="📱",
    layout="centered"
)

# 커스텀 CSS 스타일 적용
st.markdown("""
<style>
div[data-testid="stRadio"] label {
    font-size: 19px !important;
}

p {
    font-size: 18px !important;
}

h1, h2 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 1
if "recognition_score" not in st.session_state:
    st.session_state.recognition_score = 0
if "knowledge_score" not in st.session_state:
    st.session_state.knowledge_score = 0

# -----------------------------
# 1페이지 : 시작 화면
# -----------------------------
if st.session_state.page == 1:
    st.title("디지털 성범죄 예방 교육")
    st.markdown("---")
    
    st.write("""
    본 설문은 청소년의 디지털 성범죄 인식도와 예방 및 대응 지식 수준을 파악하기 위해 실시됩니다.
    
    모든 응답은 교육 프로그램 개선을 위한 자료로 활용됩니다.
    """)
    
    if st.button("시작하기", use_container_width=True):
        st.session_state.page = 2
        st.rerun()

# -----------------------------
# 2페이지 : 인식 설문
# -----------------------------
elif st.session_state.page == 2:
    st.progress(50)
    st.header("디지털 성범죄 인식 설문")
    
    options = {
        "매우 그렇다": 5,
        "그렇다": 4,
        "보통이다": 3,
        "아니다": 2,
        "전혀 아니다": 1
    }
    
    q1 = st.radio(
        "1. AI를 이용해 특정인의 얼굴을 합성한 사진이나 영상을 만드는 것이 문제라고 생각하나요?",
        list(options.keys()),
        index=None
    )
    
    q2 = st.radio(
        "2. 온라인에서 유포되는 성적인 이미지나 영상을 단순히 보는 행위도 문제라고 생각하나요?",
        list(options.keys()),
        index=None
    )
    
    q3 = st.radio(
        "3. 디지털 성범죄는 현실 세계의 성범죄만큼 피해가 심각하다고 생각하나요?",
        list(options.keys()),
        index=None
    )
    
    q4 = st.radio(
        "4. SNS에서 유행하는 챌린지나 밈도 디지털 성범죄가 될 수 있다고 생각하나요?",
        list(options.keys()),
        index=None
    )
    
    q5 = st.radio(
        "5. 친구가 다른 사람의 사진을 허락 없이 저장해 공유하는 것이 범죄가 될 수 있다고 생각하나요?",
        list(options.keys()),
        index=None
    )
    
    if st.button("다음 페이지", use_container_width=True):
        if None in [q1, q2, q3, q4, q5]:
            st.warning("모든 문항에 답변해주세요.")
        else:
            st.session_state.recognition_score = (
                options[q1] + options[q2] + options[q3] + options[q4] + options[q5]
            )
            st.session_state.page = 3
            st.rerun()

# -----------------------------
# 3페이지 : 예방 및 대응 지식
# -----------------------------
elif st.session_state.page == 3:
    st.progress(100)
    st.header("예방 및 대응 지식 설문")
    
    yes_no = {
        "예": 1,
        "아니오": 0
    }
    
    k1 = st.radio(
        "1. 디지털 성범죄 피해를 입었을 때 도움을 요청할 수 있는 기관을 3곳 이상 알고 있나요?",
        list(yes_no.keys()),
        index=None
    )
    
    k2 = st.radio(
        "2. 불법 촬영물이나 성적 이미지가 유포되었을 때 증거를 보존하는 방법을 알고 있나요?",
        list(yes_no.keys()),
        index=None
    )
    
    k3 = st.radio(
        "3. SNS 계정의 공개 범위 조정 및 개인정보 보호 설정 방법을 알고 있나요?",
        list(yes_no.keys()),
        index=None
    )
    
    k4 = st.radio(
        "4. 불법 촬영물이 포함된 게시물 혹은 계정을 신고하거나 차단하는 방법을 알고 있나요?",
        list(yes_no.keys()),
        index=None
    )
    
    k5 = st.radio(
        "5. SNS나 메신저에서 모르는 사람이 개인정보나 사진을 요구할 경우 안전하게 대처하는 방법을 알고 있나요?",
        list(yes_no.keys()),
        index=None
    )
    
    k6 = st.radio(
        "6. 디지털 성범죄 피해 사실을 신고하는 절차를 알고 있나요?",
        list(yes_no.keys()),
        index=None
    )
    
    if st.button("결과 보기", use_container_width=True):
        if None in [k1, k2, k3, k4, k5, k6]:
            st.warning("모든 문항에 답변해주세요.")
        else:
            st.session_state.knowledge_score = (
                yes_no[k1] + yes_no[k2] + yes_no[k3] + yes_no[k4] + yes_no[k5] + yes_no[k6]
            )
            st.session_state.page = 4
            st.rerun()

# -----------------------------
# 4페이지 : 결과 화면
# -----------------------------
elif st.session_state.page == 4:
    st.title("설문 결과")
    st.success("설문이 완료되었습니다.")
    
    st.markdown(
        f"<h2><b>디지털 성범죄 인식 점수 : {st.session_state.recognition_score} / 25</b></h2>",
        unsafe_allow_html=True
    )
    
    st.markdown(
        f"<h2><b>예방 및 대응 지식 점수 : {st.session_state.knowledge_score} / 6</b></h2>",
        unsafe_allow_html=True
    )
    
    st.info("설문 결과는 교육 프로그램 구성 및 개선을 위한 자료로 활용됩니다.")
    
    # 다운로드용 텍스트 파일 내용 수정
    result_text = f"""디지털 성범죄 인식 점수 : {st.session_state.recognition_score} / 25
예방 및 대응 지식 점수 : {st.session_state.knowledge_score} / 6"""
    
    st.download_button(
        label="결과 저장",
        data=result_text,
        file_name="survey_result.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    if st.button("처음으로", use_container_width=True):
        # 처음으로 돌아갈 때 점수도 함께 초기화
        st.session_state.recognition_score = 0
        st.session_state.knowledge_score = 0
        st.session_state.page = 1
        st.rerun()
