import streamlit as st
import random

# 🎮 샘플 게임 데이터
games_db = [
    {"title": "The Witcher 3", "genre": "RPG", "platform": "PC", "style": "스토리 중심"},
    {"title": "Elden Ring", "genre": "RPG", "platform": "Console", "style": "하드코어"},
    {"title": "Hades", "genre": "액션", "platform": "PC", "style": "빠른 전투"},
    {"title": "Stardew Valley", "genre": "시뮬레이션", "platform": "Mobile", "style": "힐링"},
    {"title": "Overwatch 2", "genre": "FPS", "platform": "Console", "style": "멀티플레이"},
    {"title": "Hollow Knight", "genre": "플랫폼", "platform": "PC", "style": "탐험 중심"},
    {"title": "Genshin Impact", "genre": "RPG", "platform": "Mobile", "style": "스토리 중심"},
    {"title": "Valorant", "genre": "FPS", "platform": "PC", "style": "멀티플레이"},
    {"title": "Animal Crossing", "genre": "시뮬레이션", "platform": "Console", "style": "힐링"},
]

# 🖼️ 페이지 설정
st.set_page_config(page_title="🎮 게임 추천기", page_icon="🕹️", layout="centered")

# 🌟 타이틀 영역
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🎲 오늘 뭐하고 놀까? 게임 추천기 🎮</h1>
    <p style='text-align: center;'>당신의 취향을 기반으로 최고의 게임을 추천해드려요! 💡</p>
""", unsafe_allow_html=True)

# 🎯 사용자 선택 옵션
genre = st.selectbox("🎮 선호 장르를 선택하세요:", ["RPG", "FPS", "시뮬레이션", "액션", "플랫폼"])
platform = st.selectbox("🖥️ 주로 사용하는 플랫폼은?", ["PC", "Console", "Mobile"])
style = st.selectbox("✨ 원하는 게임 스타일은?", ["스토리 중심", "하드코어", "힐링", "빠른 전투", "멀티플레이", "탐험 중심"])

# 🔍 추천 버튼
if st.button("🔍 게임 추천 받기"):
    # 필터링
    filtered_games = [game for game in games_db if game["genre"] == genre and game["platform"] == platform and game["style"] == style]
    
    # 결과 표시
    if filtered_games:
        selected = random.choice(filtered_games)
        st.success(f"🎉 추천 게임: **{selected['title']}**")
        st.markdown(f"""
        <div style="text-align: center; font-size: 1.2em; margin-top: 10px;">
            ✅ 장르: {selected['genre']} <br>
            💻 플랫폼: {selected['platform']} <br>
            ✨ 스타일: {selected['style']} <br>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("😢 해당 조건에 맞는 게임을 찾을 수 없습니다. 조건을 바꿔보세요!")

# 🎉 하단 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Streamlit</p>", unsafe_allow_html=True)
