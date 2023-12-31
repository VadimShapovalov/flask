from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str
    author: str
    description: str | None = None
    genre: str
