import streamlit as st
import random

# 🎨 페이지 기본 설정
st.set_page_config(
    page_title="가위✌️ 바위✊ 보✋ 게임",
    page_icon="🎮",
    layout="centered"
)

# 🥳 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>🎮 가위✌️ 바위✊ 보✋ 게임에 오신 걸 환영합니다! 🎉</h1>
    """,
    unsafe_allow_html=True
)

# 📢 설명
st.markdown(
    """
    <h3 style='text-align: center;'>당신의 선택은? 🤔</h3>
    <p style='text-align: center;'>컴퓨터와 한 판 붙어보세요! 누가 이길까요? 🔮</p>
    """,
    unsafe_allow_html=True
)

# 🎮 선택 옵션
choices = {
    "✌️ 가위": "scissors",
    "✊ 바위": "rock",
    "✋ 보": "paper"
}

# 🧠 결과 판단 함수
def get_result(user, computer):
    if user == computer:
        return "😐 비겼어요!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "🎉 당신이 이겼어요! 👑"
    else:
        return "😭 당신이 졌어요..."

# 🌟 컬러 박스로 구분
st.markdown("---")
st.subheader("👇 아래에서 하나를 선택하세요!")

# 🎲 사용자 선택
user_choice_emoji = st.radio("",
    list(choices.keys()),
    index=0,
    horizontal=True,
    label_visibility="collapsed"
)

user_choice = choices[user_choice_emoji]

# 🕹️ 게임 실행 버튼
if st.button("🎲 게임 시작!"):
    computer_choice = random.choice(list(choices.values()))
    result = get_result(user_choice, computer_choice)

    # ✨ 애니메이션 느낌 출력
    with st.spinner("컴퓨터가 고민 중... 🤔"):
        st.sleep(1.5)

    # 🎯 결과 출력
    st.success(f"당신의 선택: {user_choice_emoji}")
    
    comp_choice_emoji = [k for k, v in choices.items() if v == computer_choice][0]
    st.info(f"컴퓨터의 선택: {comp_choice_emoji}")

    st.markdown(
        f"<h2 style='text-align: center; color: #33cc33;'>{result}</h2>",
        unsafe_allow_html=True
    )

# 🎨 하단 푸터
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Made with ❤️ by Streamlit</p>",
    unsafe_allow_html=True
)
