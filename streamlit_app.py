import streamlit as st
import pandas as pd
from graphviz import Digraph

# 🎨 Фонове зображення + стиль для label
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

/* СТИЛЬ ДЛЯ label (фільтри) */
label {
    color: #00BFFF !important;
    text-shadow: 0px 1px 3px rgba(0,0,0,0.6);
    font-weight: 700 !important;
    background-color: rgba(255, 255, 255, 0.3);
    padding: 6px 10px;
    border-radius: 8px;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

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
st.markdown("---")
st.subheader("🧠 Mind Map – Основні інсайти з книги")

dot = Digraph()
dot.attr(bgcolor='white')
dot.attr('node', shape='box', style='filled', fontname='Arial', color='lightblue')
dot.node("Книга", "📘 Можливо все")

# Показати перші 10 рядків
for i, row in df.head(10).iterrows():
    chapter = row["Назва розділу"] if "Назва розділу" in row and pd.notna(row["Назва розділу"]) else f"Розділ {i}"
    insight = str(row["Інсайти"]).strip() if "Інсайти" in row and pd.notna(row["Інсайти"]) else ""
    author = str(row["Учасник"]).strip() if "Учасник" in row and pd.notna(row["Учасник"]) else ""

    if chapter and insight:
        chapter_node = f"chapter_{i}"
        insight_node = f"insight_{i}"

        dot.node(chapter_node, f"📖 {chapter}", color='lightgreen')
        dot.edge("Книга", chapter_node)

        short = insight[:60] + "..." if len(insight) > 60 else insight
        dot.node(insight_node, f"💡 {short}\n👤 {author}", color='lightyellow')
        dot.edge(chapter_node, insight_node)

st.graphviz_chart(dot)
