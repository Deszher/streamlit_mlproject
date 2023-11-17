# https://huggingface.co/WelfCrozzo/T5-L128-belarusian
from fastapi import FastAPI
from pydantic import BaseModel
from translator import Translator
from fastapi.responses import HTMLResponse


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    result: str


translator = Translator()

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>FastAPI ML project</title>
        </head>
        <body>
            <h1>FastAPI ML project</h1
            <p>See API documentation in <a href="/docs">OpenAPI schema</a></p>
        </body>
    </html>
    """


@app.post("/predict/")
def predict(request: PredictRequest) -> PredictResponse:
    """Модель для перевода текста с русского на белорусский язык. Введите текст на русском языке (например):
     'Не ищи счастье – оно всегда у тебя внутри'
    Источник - https://huggingface.co/WelfCrozzo/T5-L128-belarusian"""

    result = translator.translate(request.text)

    return PredictResponse(result=result)

# uvicorn main_fast_api:app
