# streamlit_mlproject
_________________________________________
## Приложение по переводу текста с русского на белорусский язык.
Web-приложение на основе библиотеки Streamlit и API-сервер на основе FastAPI, которые используют библиотеку машинного обучения: Hugging Face.
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
docker build -t mlproject_base -f Dockerfile_base .
docker build -t mlproject_streamlit -f Dockerfile_streamlit .

# Запускаем контейнер
docker run -p 8501:8501 mlproject_streamlit
```

 Веб сервер будет доступен по адресу http://localhost:8501/

## Запуск ML fastapi

For dev

```bash
uvicorn main_fast_api:app --reload
```

### Использование с докером
```bash
# Собираем образ
docker build -t mlproject_base -f Dockerfile_base .
docker build -t mlproject_fastapi -f Dockerfile_fastapi .

# Запускаем контейнер
docker run -p 8000:8000 mlproject_fastapi
```

FastAPI сервер будет доступен по адресу http://127.0.0.1:8000/

## Тестирование

```bash
pytest
```


