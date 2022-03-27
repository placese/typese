from typing import Optional
import random

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path


from utils import texts_russian, texts_english

app = FastAPI()

print(Path(__file__).parent.parent.absolute())
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory='templates')

@app.get("/type")
async def type(request: Request, lang: Optional[str] = 'eng'):
    print(lang)
    if lang == 'rus':
        text = random.choice(texts_russian)
    else:
        text = random.choice(texts_english)
    return templates.TemplateResponse("index.html", {"request": request, "text": text.replace("\n", " ")})

@app.post('/select_language')
async def select_language(request: Request, lang: str = Form('eng')):
    return await type(request=request, lang=lang)
