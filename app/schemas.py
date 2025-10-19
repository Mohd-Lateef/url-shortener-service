from pydantic import BaseModel
from datetime import datetime


class URLCreate(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: datetime
