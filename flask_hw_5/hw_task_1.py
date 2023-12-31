import os
import json
from pathlib import Path
import aiofiles
from pydantic import TypeAdapter
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .pydantic_models import  Book


BASE_DIR = Path(__file__).resolve().parent
json_file = os.path.join(BASE_DIR, 'books.json')

if not os.path.exists(json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=2)

with open(json_file, encoding='utf-8') as f:
    json_data = json.load(f)

app = FastAPI()
templates = Jinja2Templates('flask_hw/flask_hw_5/templates')
# templates = Jinja2Templates('hw_5/templates')
type_adapter = TypeAdapter(Book)
books: list[Book] = [type_adapter.validate_python(book) for book in json_data]


async def commit_changes():
    async with aiofiles.open(json_file, 'w', encoding='utf-8') as f:
        json_book = [book.model_dump(mode='json') for book in books]
        content = json.dumps(json_book, ensure_ascii=False, indent=2)
        await f.write(content)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        'main.html', {'request': request, 'books': books}
    )


@app.post('/books/')
async def add_book(book: Book):
    books.append(book)
    await commit_changes()
    return book


@app.get('/books/{book_id}', response_class=HTMLResponse)
async def get_book(request: Request, book_id: int):
    filtered_book = [book for book in books if book.id == book_id]

    if not filtered_book:
        book = None
    else:
        book = filtered_book[0]

    return templates.TemplateResponse(
        'books.html', {'request': request, 'book': book}
    )


@app.put('/books/{book_id}')
async def update_book(book_id: int, new_book: Book):
    filtered_book = [book for book in books if book.id == book_id]

    if not filtered_book:
        return {'updated': False}

    book = filtered_book[0]

    book.name = new_book.name
    book.author = new_book.author
    book.description = new_book.description
    book.genre = new_book.genre

    await commit_changes()

    return {'updated': True, 'book': new_book}


@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    filtered_book = [book for book in books if book.id == book_id]

    if not filtered_book:
        return {'deleted': False}

    book = filtered_book[0]
    books.remove(book)

    await commit_changes()

    return {'deleted': True, 'book': book}
