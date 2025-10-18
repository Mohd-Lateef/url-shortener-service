from pydantic import BaseModel


class URLCreate(BaseModel):
    id: int
    original_url: str
    short_code: str
