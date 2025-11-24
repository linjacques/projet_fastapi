from fastapi import APIRouter
from typing import Optional
from src.services.book import BookService
from src.models.book import Book, BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[Book])
def list_books(
    author: Optional[str] = None,
    year: Optional[int] = None,
    title_contains: Optional[str] = None,
):
    return BookService.list_books(author, year, title_contains)


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    return BookService.get_book(book_id)


@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    return BookService.create_book(book)


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookUpdate):
    return BookService.update_book(book_id, book_data)


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    BookService.delete_book(book_id)
    return
