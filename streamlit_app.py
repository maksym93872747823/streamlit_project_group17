import streamlit as st
import pandas as pd
from graphviz import Digraph

# 🌄 Фонове зображення
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/maksym93872747823/streamlit_project_group17/main/mountain_bg.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# 🎨 Стилі
st.markdown('''
<style>
/* Стиль selectbox */
div[data-baseweb="select"] {
    background-color: rgba(255, 255, 255, 0.85) !important;
    border-radius: 8px !important;
    padding: 4px !important;
}
/* Текст label */
label {
    background-color: rgba(255, 255, 255, 0.85) !important;
    color: #000000 !important;
    font-weight: 600 !important;
    padding: 6px 10px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 4px;
}
/* Заголовки */
h1, .st-subheader, h2 {
    color: #000000 !important;
}
/* Повні інсайти - контейнер */
.insight-block {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    margin-top: 40px;
}
/* Expander */
.streamlit-expander {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    margin-top: 12px;
}
.streamlit-expanderHeader {
    font-weight: bold;
    color: #000000 !important;
    background-color: rgba(255, 255, 255, 0.6) !important;
    padding: 10px;
    border-radius: 10px !important;
}
</style>
''', unsafe_allow_html=True)

# 📘 Заголовок
st.markdown("""
    <h1 style='text-align: center; color: #F9FAFB;'>📚 <span style='color:#00BFFF'>Можливо все</span></h1>
    <p style='text-align: center; font-size:18px; color: #000000; background-color: rgba(255,255,255,0.6); padding: 10px; border-radius: 8px;'>
        Цитати, ідеї та натхнення, зібрані нашою командою під час аналізу книги.
    </p>
    <hr style='border: 1px solid #444;'/>
""", unsafe_allow_html=True)

# 📊 Завантаження даних
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3cQlzWgr-dv_MC_usm7D2Lr2-XGG7HosOcMvLMQF3_e672gdHaTo8jxpJ77fwrPrwjKNyRh53IjLT/pub?output=csv"
df = pd.read_csv(url)

# 🧍‍♀️ Фільтр по учаснику
if "Учасник" in df.columns:
    selected_author = st.selectbox("Обрати учасника", ["Всі"] + sorted(df["Учасник"].dropna().unique()))
    if selected_author != "Всі":
        df = df[df["Учасник"] == selected_author]

# 📚 Фільтр по розділу
if "Назва розділу" in df.columns:
    selected_chapter = st.selectbox("Обрати розділ", ["Всі"] + sorted(df["Назва розділу"].dropna().unique()))
    if selected_chapter != "Всі":
        df = df[df["Назва розділу"] == selected_chapter]

# 🧾 Таблиця
st.subheader("Результати після фільтрації")
st.dataframe(df)

# 🧠 Mind Map
st.markdown("---")
st.markdown(
    "<h2 style='text-align: center; color: black; background-color: rgba(255,255,255,0.8); padding: 8px; border-radius: 10px;'>🧠 Mind Map – Основні інсайти з книги</h2>",
    unsafe_allow_html=True
)

dot = Digraph()
dot.attr(rankdir='LR')
dot.attr(bgcolor='white')
dot.attr('node', shape='box', style='filled', fontname='Arial', fontsize='11', color='lightblue')
dot.node("Книга", "📘 Можливо все")

for i, row in df.head(10).iterrows():
    chapter = row.get("Назва розділу", f"Розділ {i}")
    insight = str(row.get("Інсайти", "")).strip()
    author = str(row.get("Учасник", "")).strip()

    if chapter and insight:
        chapter_node = f"chapter_{i}"
        insight_node = f"insight_{i}"

        dot.node(chapter_node, f"📖 {chapter}", color='lightgreen')
        dot.edge("Книга", chapter_node)

        short = insight[:70] + "..." if len(insight) > 70 else insight
        dot.node(insight_node, f"💡 {short}\n👤 {author}", color='lightyellow')
        dot.edge(chapter_node, insight_node)

st.graphviz_chart(dot, use_container_width=True)

# 🔍 Повні інсайти
with st.container():
    st.markdown("""<div class="insight-block"><h3 style='color: #000000;'>🔍 Повні інсайти</h3>""", unsafe_allow_html=True)

    for i, row in df.head(10).iterrows():
        chapter = row.get("Назва розділу", f"Розділ {i}")
        insight = str(row.get("Інсайти", "")).strip()
        author = str(row.get("Учасник", "")).strip()

        if chapter and insight:
            with st.expander(f"📖 {chapter} – {author}"):
                st.markdown(f"""
                    <div style="background-color: rgba(255,255,255,0.95); padding: 15px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); color: #000000;">
                        {insight}
                    </div>
                """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
# 📖 Розділи книги — у стилі Повні інсайти
st.markdown("---")
st.markdown("<h3 style='color: #000000;'>📖 Розділи книги</h3>", unsafe_allow_html=True)

chapters = [
    "ВСТУП – Аліна",
    "РОЗДІЛ 1. Чи можливо, що можливо все? – Анна Котова",
    "РОЗДІЛ 2. «Вітер змін» – Максим Петроченко",
    "РОЗДІЛ 3. Початок відліку — у голові – Інна / Христина",
    "РОЗДІЛ 4. Що для мене найважливіше? – Анжела",
    "РОЗДІЛ 5. Розберімося, чого ви насправді хочете! – Анна Кіншова",
    "РОЗДІЛ 6. Час діяти! – Рома",
    "РОЗДІЛ 7. «Уперед і тільки вперед!» – Віталій / Лєна",
    "РОЗДІЛ 8. Рішення — ключ до неможливого – Іван",
    "РОЗДІЛ 9. «Та на все це життя не вистачить!» – Ганна Т."
]

for title in chapters:
    with st.expander(""):
        st.markdown(f"""
        <div style="
            background-color: rgba(255,255,255,0.95);
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            color: #000000;
            font-weight: bold;
        ">
            📖 {title}
            <p style="font-weight: normal; margin-top: 10px;">
                Тут можна додати короткий опис, цитати, нотатки або рефлексії по цьому розділу.
            </p>
        </div>
        """, unsafe_allow_html=True)


