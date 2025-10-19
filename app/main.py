from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .crud import create_url, redirect_url

app = FastAPI()
print("main.py loaded")


@app.post("/ShortenURL")
def create_url_endpoint(url: str, db: Session = Depends(get_db)):
    return create_url(url, db)


@app.get("/{shortCode}")
def redirect_to_originalUrl(shortCode: str, db: Session = Depends(get_db)):
    return redirect_url(shortCode, db)
