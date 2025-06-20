"""
Streamlit приложение
"""

from json import loads
from logging.handlers import TimedRotatingFileHandler
import requests
import pandas as pd
import streamlit as st
from PIL import Image


class ServerException(Exception):
    pass




st.write(
    """
        # 🤓 Подготовка к экзамену
        📝 Установите параметры экзамена и приступайте!
        """
)


def process_main_page():
    """
    Рендеринг основных элементов страницы
    (заголовки, изображения, sidebar, кнопки)
    """
    image = Image.open("exam_photo.jpg")
    st.image(image)
    process_side_bar()
    easy_df = st.session_state.get('easy_df', None)
    hard_df = st.session_state.get('hard_df', None)
    if easy_df is not None:
        st.write('Пример простых вопросов (дебильник):')
        st.table(easy_df)
    if hard_df is not None:
        st.write('Пример сложных вопросов:')
        st.table(hard_df)


def process_side_bar():
    st.sidebar.header(
        "Параметры экзамена")
    sidebar_input_features()

def sidebar_input_features():
    """
    Рендеринг формы для загрузки данных через csv файл
    или через выбор параметров вручную
    """

    easy_questions_num = st.sidebar.number_input("Количество простых вопросов", 0, 10, 3)
    hard_questions_num = st.sidebar.number_input("Количество сложных вопросов", 0, 10, 0)
    st.session_state['easy_questions_num'] = easy_questions_num
    st.session_state['hard_questions_num'] = hard_questions_num

    if easy_questions_num > 0:
        easy_file = st.sidebar.file_uploader(label="Загрузить excel-файл простых вопросов", type=["xlsx"])
        if easy_file is not None:
            easy_df = pd.read_excel(easy_file)
            st.session_state['easy_df'] = easy_df
    else:
        easy_df = None
        st.session_state['easy_df'] = easy_df

    if hard_questions_num > 0:
        hard_file = st.sidebar.file_uploader(label="Загрузить excel-файл сложных вопросов", type=["xlsx"])
        if hard_file is not None:
            hard_df = pd.read_excel(hard_file)   
            st.session_state['hard_df'] = hard_df
    else:
        hard_df = None
        st.session_state['hard_df'] = hard_df
    
    st.sidebar.page_link("pages/exam.py", label="**Перейти к экзамену**", icon="➡️")

if __name__ == "__main__":
    process_main_page()