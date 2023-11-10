# streamlit_mlproject
_________________________________________
## Приложение по переводу текста с русского на белорусский язык.
Web-приложение на основе библиотеки Streamlit, которое использует библиотеку машинного обучения: Hugging Face.
T5 for belarusian language

## Запуск WEB-приложения streamlit

### Использование без докера
Сначала нужно установить anaconda https://docs.anaconda.com/free/anaconda/install/mac-os/
```bash
# Без venv
# Устанавливаем зависимости
pip install -r requirements.txt
# Запускаем WEB-приложение
streamlit run main.py

# С venv
# Создаем venv
python3 -m venv .venv
source .venv/bin/activate
# Устанавливаем зависимости в venv
pip install -r requirements.txt
# Запускаем WEB-приложение
streamlit run main.py
```

### Использование с докером
```bash
# Собираем образ
docker build -t streamlit_mlproject .

# Запускаем
docker run -p 8501:8501 streamlit_mlproject
```

 Веб сервер будет доступен по адресу http://localhost:8501/