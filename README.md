# streamlit_mlproject
_________________________________________
## Приложение по переводу текста с русского на белорусский язык.
Web приложение на основе библиотеки Streamlit и API-сервер на основе FastAPI, которые используют библиотеку машинного обучения: Hugging Face.
T5 for belarusian language

## Deploy pipeline

FastAPI production host: https://api.ml1.webtm.ru/
Streamlit production host: https://streamlit.ml1.webtm.ru/

Разворачивается при мерже/пуше в ветки main/develop изменений с использованием github actions.

## Локальный запуск WEB-приложения streamlit

### Использование без докера
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
docker build -t mlproject_streamlit --build-arg DEPS_IMAGE=mlproject_base -f Dockerfile_streamlit .

# Запускаем контейнер
docker run -p 8501:8501 mlproject_streamlit
```

 Веб сервер будет доступен по адресу http://localhost:8501/

## Локальный запуск ML fastapi

For dev

```bash
uvicorn main_fast_api:app --reload
```

### Использование с докером
```bash
# Собираем образ
docker build -t mlproject_base -f Dockerfile_base .
docker build -t mlproject_fastapi --build-arg DEPS_IMAGE=mlproject_base -f Dockerfile_fastapi .

# Запускаем контейнер
docker run -p 8000:8000 mlproject_fastapi
```

FastAPI сервер будет доступен по адресу http://127.0.0.1:8000/

Документация доступна по адресу http://127.0.0.1:8000/docs

## Тестирование

```bash
pytest
```


