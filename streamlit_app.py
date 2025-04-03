import streamlit as st
import pandas as pd

# Заголовок
st.markdown(
    """
    <h1 style='text-align: center; color: #F9FAFB;'>📚 <span style='color:#00BFFF'>Можливо все</span></h1>
    <p style='text-align: center; font-size:18px; color: #D1D5DB;'>
        Цитати, ідеї та натхнення, зібрані нашою командою під час аналізу книги.
    </p>
    <hr style='border: 1px solid #444;'/>
    """,
    unsafe_allow_html=True
)

# Подключение Google Таблицы
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3cQlzWgr-dv_MC_usm7D2Lr2-XGG7HosOcMvLMQF3_e672gdHaTo8jxpJ77fwrPrwjKNyRh53IjLT/pub?output=csv"
df = pd.read_csv(url)

# Выводим таблицу на сайт
st.subheader("Актуальні дані з таблиці")
st.dataframe(df)

