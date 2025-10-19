from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends, HTTPException
from fastapi.responses import RedirectResponse
from utils import Base62, checkIfExists
import models


def create_url(url: str, db: Session):
    existing = checkIfExists(url, db)
    if existing:
        return f"localhost:8000{existing.short_code}"
    else:
        new_url = models.URLCreate(original_url=url)
        db.add(new_url)
        db.commit()
        db.refresh(new_url)
        new_url.short_code = Base62(new_url.id)
        db.add(new_url)
        db.commit()
        return f"localhost:8000/{new_url.short_code}"


def redirect_url(shortcode: str, db: Session ):
    urlEntry = (
        db.query(models.URLCreate)
        .filter(models.URLCreate.short_code == shortcode)
        .first()
    )
    if urlEntry:
        return RedirectResponse(url=urlEntry.original_url,status_code=307)
    else:
        raise HTTPException(status_code=404, detail="URL not found")
