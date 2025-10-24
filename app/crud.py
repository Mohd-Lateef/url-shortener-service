from sqlalchemy.orm import Session
from .database import get_db
from fastapi import Depends, HTTPException
from fastapi.responses import RedirectResponse,PlainTextResponse
from .utils import Base62, checkIfExists
from . import models


def create_url(url: str, db: Session):
    existing = checkIfExists(url, db)
    if existing:
        return PlainTextResponse(content=f"http://localhost:8000/{existing.short_code}")
    else:
        new_url = models.URLModel(original_url=url)
        db.add(new_url)
        db.commit()
        db.refresh(new_url)
        new_url.short_code = Base62(new_url.id)
        db.commit()
        return PlainTextResponse(content=f"http://localhost:8000/{new_url.short_code}")


def redirect_url(shortcode: str, db: Session):
    urlEntry = (
        db.query(models.URLModel)
        .filter(models.URLModel.short_code == shortcode)
        .first()
    )
    if urlEntry:
        return RedirectResponse(url=urlEntry.original_url, status_code=307)
    else:
        raise HTTPException(status_code=404, detail="URL not found")
