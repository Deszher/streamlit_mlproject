"""
# Our first app
"""

import time
from translator import Translator

import streamlit as st
from transformers import pipeline

translator = Translator()

#  логотип и название
col1, col2 = st.columns([1, 1])

with col1:
    st.header('Model "ML translation RuBe"')

with col2:
    st.image("assets/unn.jpg")

# Боковая панель
st.sidebar.image("assets/T5.png", width=100)
st.sidebar.title("About the project:")
st.sidebar.info(
    """
    This model is based on T5-small with sequence length equal 128 tokens.  
    (https://huggingface.co/WelfCrozzo/T5-L128-belarusian). 
    """
)

st.sidebar.info(
    """
    Model trained from scratch on RTX 3090 24GB
    """
)

st.sidebar.info(
    """
    Вы можете воспользоваться данным приложением для перевода текста с русского на белорусский язык
    """
)

# Ввод текста
inp = st.text_input('Введите текст на русском языке (например):', 'Не ищи счастье – оно всегда у тебя внутри')
run_button = st.button(label='Run')

# если нажата кнопка, то пауза 2 сек., запуск шариков, печать текста и перевод
if run_button:
    with st.spinner('Wait for it...'):
        time.sleep(2)
        text = translator.translate(inp)
    st.balloons()
    st.success(f"'{inp}' в переводе на белорусский язык означает:")

    st.write(text)

# streamlit run main.py
# streamlit run C:/Users/Админ/PycharmProjects/fill-mask/main.py
