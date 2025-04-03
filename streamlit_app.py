import streamlit as st
import pandas as pd
from graphviz import Digraph

# Фонове зображення
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/maksym93872747823/streamlit_project_group17/main/mountain_bg.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    min-height: 100vh;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Стиль для селекторів та заголовків
st.markdown("""
    <style>
    .stSelectbox > div > div {
        color: black !important;
        background-color: rgba(255,255,255,0.8) !important;
        border-radius: 8px;
        padding: 5px;
    }
    .stSelectbox label {
        color: black !important;
        font-weight: bold;
    }
    .st-subheader, h2, h3, h4 {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown(
    """
    <h1 style='text-align: center; color: #F9FAFB;'>📚 <span style='color:#00BFFF'>Можливо все</span></h1>
    <p style='text-align: center; font-size:18px; color: #000000; background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 8px;'>
        Цитати, ідеї та натхнення, зібрані нашою командою під час аналізу книги.
    </p>
    <hr style='border: 1px solid #444;'/>
    """,
    unsafe_allow_html=True
)

# Підключення Google Таблиці
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3cQlzWgr-dv_MC_usm7D2Lr2-XGG7HosOcMvLMQF3_e672gdHaTo8jxpJ77fwrPrwjKNyRh53IjLT/pub?output=csv"
df = pd.read_csv(url)

# Фільтр по учаснику
if "Учасник" in df.columns:
    selected_author = st.selectbox("Обрати учасника", ["Всі"] + sorted(df["Учасник"].dropna().unique()))
    if selected_author != "Всі":
        df = df[df["Учасник"] == selected_author]

# Фільтр по назві розділу
if "Назва розділу" in df.columns:
    selected_chapter = st.selectbox("Обрати розділ", ["Всі"] + sorted(df["Назва розділу"].dropna().unique()))
    if selected_chapter != "Всі":
        df = df[df["Назва розділу"] == selected_chapter]

# Вивід таблиці
st.subheader("Результати після фільтрації")
st.dataframe(df)

# Mind Map
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<h2 style='text-align: center; color: black; background-color: rgba(255, 255, 255, 0.7); padding: 8px; border-radius: 10px;'>🧠 Mind Map – Основні інсайти з книги</h2>",
    unsafe_allow_html=True
)

dot = Digraph()
dot.attr(rankdir='LR')  # Горизонтально
dot.attr(bgcolor='white')
dot.attr('node', shape='box', style='filled', fontname='Arial', fontsize='12', color='lightblue')

dot.node("Книга", "📘 Можливо все")

# Показати перші 10 рядків
for i, row in df.head(10).iterrows():
    chapter = row["Назва розділу"] if "Назва розділу" in row and pd.notna(row["Назва розділу"]) else f"Розділ {i}"
    insight = str(row["Інсайти"]).strip() if "Інсайти" in row and pd.notna(row["Інсайти"]) else ""
    author = str(row["Учасник"]).strip() if "Учасник" in row and pd.notna(row["Учасник"]) else ""
