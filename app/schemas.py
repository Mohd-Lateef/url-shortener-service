from pydantic import BaseModel
from datetime import datetime


class URLCreate(BaseModel):
    original_url: str
