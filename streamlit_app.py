import streamlit as st
import pandas as pd

# Фоновое изображение
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/maksym93872747823/streamlit_project_group17/main/mountain_bg.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    min-height: 100vh; /* Покрывает весь экран */
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


# Подключение Google Таблицы
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3cQlzWgr-dv_MC_usm7D2Lr2-XGG7HosOcMvLMQF3_e672gdHaTo8jxpJ77fwrPrwjKNyRh53IjLT/pub?output=csv"
df = pd.read_csv(url)

# Фільтри
if "Ім'я" in df.columns:
    selected_author = st.selectbox("Обрати учасника", ["Всі"] + sorted(df["Ім'я"].dropna().unique()))
    if selected_author != "Всі":
        df = df[df["Ім'я"] == selected_author]

if "Назва розділу" in df.columns:
    selected_chapter = st.selectbox("Обрати розділ", ["Всі"] + sorted(df["Назва розділу"].dropna().unique()))
    if selected_chapter != "Всі":
        df = df[df["Назва розділу"] == selected_chapter]

# Виведення таблиці після фільтрації
st.subheader("Результати після фільтрації")
st.dataframe(df)

# Вивід таблиці після фільтрації
st.subheader("Результати після фільтрації")
st.dataframe(df)
