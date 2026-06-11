
import streamlit as st

st.set_page_config(
    page_title="디지털 성범죄 예방 교육",
    page_icon="📱",
    layout="centered"
)

# 페이지 상태 저장
if "page" not in st.session_state:
    st.session_state.page = 1

# -----------------------------
# 1페이지
# -----------------------------
if st.session_state.page == 1:

    st.title("디지털 성범죄 예방 교육")

    st.markdown("---")

    st.markdown("""
    본 설문은 청소년의 디지털 성범죄 인식도와
    예방 및 대응 지식 수준을 파악하기 위해 실시됩니다.

    아래 버튼을 눌러 시작해주세요.
    """)

    if st.button("시작하기"):
        st.session_state.page = 2
        st.rerun()

# -----------------------------
# 2페이지
# -----------------------------
elif st.session_state.page == 2:

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
        options.keys()
    )

    q2 = st.radio(
        "2. 온라인에서 유포되는 성적인 이미지나 영상을 단순히 보는 행위도 문제라고 생각하나요?",
        options.keys()
    )

    q3 = st.radio(
        "3. 디지털 성범죄는 현실 세계의 성범죄만큼 피해가 심각하다고 생각하나요?",
        options.keys()
    )

    q4 = st.radio(
        "4. SNS에서 유행하는 챌린지나 밈도 디지털 성범죄가 될 수 있다고 생각하나요?",
        options.keys()
    )

    q5 = st.radio(
        "5. 친구가 다른 사람의 사진을 허락 없이 저장해 공유하는 것이 범죄가 될 수 있다고 생각하나요?",
        options.keys()
    )

    if st.button("다음 페이지"):
        st.session_state.recognition_score = (
            options[q1] +
            options[q2] +
            options[q3] +
            options[q4] +
            options[q5]
        )

        st.session_state.page = 3
        st.rerun()

# -----------------------------
# 3페이지
# -----------------------------
elif st.session_state.page == 3:

    st.header("예방 및 대응 지식 설문")

    yes_no = {
        "예": 1,
        "아니오": 0
    }

    k1 = st.radio(
        "1. 디지털 성범죄 피해를 입었을 때 도움을 요청할 수 있는 기관을 3곳 이상 알고 있나요?",
        yes_no.keys()
    )

    k2 = st.radio(
        "2. 불법 촬영물이나 성적 이미지가 유포되었을 때 증거를 보존하는 방법을 알고 있나요?",
        yes_no.keys()
    )

    k3 = st.radio(
        "3. SNS 계정의 공개 범위 조정 및 개인정보 보호 설정 방법을 알고 있나요?",
        yes_no.keys()
    )

    k4 = st.radio(
        "4. 불법 촬영물이 포함된 게시물 혹은 계정을 신고하거나 차단하는 방법을 알고 있나요?",
        yes_no.keys()
    )

    k5 = st.radio(
        "5. SNS나 메신저에서 모르는 사람이 개인정보나 사진을 요구할 경우 안전하게 대처하는 방법을 알고 있나요?",
        yes_no.keys()
    )

    k6 = st.radio(
        "6. 디지털 성범죄 피해 사실을 신고하는 절차를 알고 있나요?",
        yes_no.keys()
    )

    if st.button("결과 확인"):

        knowledge_score = (
            yes_no[k1] +
            yes_no[k2] +
            yes_no[k3] +
            yes_no[k4] +
            yes_no[k5] +
            yes_no[k6]
        )

        recognition_score = st.session_state.recognition_score

        # 인식 수준
        if recognition_score >= 20:
            recognition_level = "높음"
        elif recognition_score >= 13:
            recognition_level = "보통"
        else:
            recognition_level = "낮음"

        # 지식 수준
        if knowledge_score >= 5:
            knowledge_level = "높음"
        elif knowledge_score >= 3:
            knowledge_level = "보통"
        else:
            knowledge_level = "낮음"

        st.success("설문 완료!")

        st.subheader("설문 결과")

        st.write(
            f"디지털 성범죄 인식도: {recognition_score}점 ({recognition_level})"
        )

        st.write(
            f"예방 및 대응 지식: {knowledge_score}점 ({knowledge_level})"
        )
