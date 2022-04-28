import random

from fastapi import Depends, FastAPI, Form, Query, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine
from app.database import models, schemas, crud

from utils import texts_russian, texts_english


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = {
    'http://localhost',
    'http://localhost:3000',
}

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory='templates')


@app.get("/type", response_class=HTMLResponse)
async def type_main(request: Request, lang: str = Query('eng')) -> str:
    """
    later
    """
    print(lang)
    if lang == 'rus':
        text = random.choice(texts_russian).replace("ё", "е")
    else:
        text = random.choice(texts_english)
    print(request.query_params)
    response = templates.TemplateResponse(
        "index.html",
        {"request": request, "text": text.replace("\n", " "), "lang": lang}
    )
    return response
    

@app.post('/select_language')
async def select_language(request: Request, lang: str = Form('eng')) -> str:
    return await type_main(request=request, lang=lang)


@app.post('/register/', response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.User:
    
    if crud.get_user_by_email(db=db, user_email=user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with such email already exists"
        )
    if crud.get_user_by_user_name(db=db, user_name=user.user_name):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with such user_name already exists"
        )
    return crud.create_user(db=db, user=user)
