# https://huggingface.co/WelfCrozzo/T5-L128-belarusian
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

translator = pipeline("translation", model="WelfCrozzo/T5-L128-belarusian")


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "All right, there is a connection."}


@app.post("/predict/")
def predict(item: Item):
    """Модель для перевода текста с русского на белорусский язык. Введите текст на русском языке (например):
     'Не ищи счастье – оно всегда у тебя внутри'
    Источник - https://huggingface.co/WelfCrozzo/T5-L128-belarusian"""

    return translator(item.text, 50)[0]['translation_text']

# uvicorn main_fast_api:app
