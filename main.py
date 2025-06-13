import streamlit as st
import random

# 추천할 게임 목록 (장르별)
game_data = {
    "RPG": ["The Witcher 3", "Final Fantasy XV", "Elden Ring"],
    "FPS": ["Call of Duty", "Valorant", "Counter-Strike 2"],
    "시뮬레이션": ["The Sims 4", "Cities: Skylines", "Microsoft Flight Simulator"],
    "전략": ["StarCraft II", "Civilization VI", "Age of Empires IV"],
    "스포츠": ["FIFA 24", "NBA 2K24", "eFootball 2024"],
    "인디": ["Hollow Knight", "Celeste", "Stardew Valley"],
    "호러": ["Resident Evil Village", "Phasmophobia", "Outlast"]
}

st.title("🎮 게임 추천 웹 앱")
st.write("당신의 선호 장르를 선택하면, 추천 게임을 알려드릴게요!")

# 장르 선택 UI
selected_genres = st.multiselect(
    "선호하는 장르를 선택하세요 (복수 선택 가능):",
    options=list(game_data.keys())
)

# 추천 버튼
if st.button("게임 추천받기"):
    if not selected_genres:
        # 아무 장르도 선택하지 않았을 경우
        random_genre = random.choice(list(game_data.keys()))
        game = random.choice(game_data[random_genre])
        st.warning("장르를 선택하지 않으셔서 랜덤 추천을 드려요!")
        st.success(f"추천 게임: **{game}** (장르: {random_genre})")
    else:
        # 선택한 장르에서 무작위 추천
        recommended_games = []
        for genre in selected_genres:
            if genre in game_data:
                game = random.choice(game_data[genre])
                recommended_games.append((genre, game))

        st.subheader("🎯 추천 게임 목록:")
        for genre, game in recommended_games:
            st.write(f"- **{game}** (장르: {genre})")

