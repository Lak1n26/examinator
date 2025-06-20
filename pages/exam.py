
from json import loads
from logging.handlers import TimedRotatingFileHandler
import requests
import pandas as pd
import streamlit as st
from PIL import Image


def process_main_page():
    st.write('# Экзамен начался!')
    easy_questions_num = st.session_state.get('easy_questions_num', None)
    hard_questions_num = st.session_state.get('hard_questions_num', None)
    st.write(f'У вас будет {easy_questions_num} простых вопросов и {hard_questions_num} сложных вопросов')
    
    easy_df = st.session_state.get('easy_df', None)
    hard_df = st.session_state.get('hard_df', None)

    if easy_df is not None:
        easy_questions_for_exam = easy_df.sample(easy_questions_num).reset_index(drop=True)
        for i, row in easy_questions_for_exam.iterrows():
            question, answer = row['Вопрос'], row['Правильный ответ']
            question_expander = st.expander(f'Простой вопрос № {i+1} - {question}')
            with question_expander:
                st.write('Правильный ответ:')
                st.write(answer)

    if hard_df is not None:
        hard_questions_for_exam = hard_df.sample(hard_questions_num).reset_index(drop=True)
        for i, row in hard_questions_for_exam.iterrows():
            question, answer = row['Вопрос'], row['Правильный ответ']
            question_expander = st.expander(f'Сложный вопрос № {i+1} - {question}')
            with question_expander:
                st.write('Правильный ответ:')
                st.write(answer)
    

if __name__ == "__main__":
    process_main_page()