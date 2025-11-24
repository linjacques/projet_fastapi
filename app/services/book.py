from fastapi import HTTPException
from src.models.book import Book, BookCreate, BookUpdate

books = [
    Book(id=1, title="Le Petit Prince", author="Antoine de Saint-Exupéry", year=1943),
    Book(id=2, title="1984", author="George Orwell", year=1949),
    Book(id=3, title="Harry Potter à l'école des sorciers", author="J.K. Rowling", year=1997),
]

next_id = 4


class BookService:

    @staticmethod
    def list_books(author=None, year=None, title_contains=None):
        results = books

        if author:
            results = [b for b in results if author.lower() in b.author.lower()]
        if year:
            results = [b for b in results if b.year == year]
        if title_contains:
            results = [b for b in results if title_contains.lower() in b.title.lower()]

        return results

    @staticmethod
    def get_book(book_id: int):
        for book in books:
            if book.id == book_id:
                return book
        raise HTTPException(status_code=404, detail="Livre non trouvé")

    @staticmethod
    def create_book(book_data: BookCreate):
        global next_id
        new_book = Book(id=next_id, **book_data.dict())
        books.append(new_book)
        next_id += 1
        return new_book

    @staticmethod
    def update_book(book_id: int, book_data: BookUpdate):
        for book in books:
            if book.id == book_id:
                if book_data.title is not None:
                    book.title = book_data.title
                if book_data.author is not None:
                    book.author = book_data.author
                if book_data.year is not None:
                    book.year = book_data.year
                return book

        raise HTTPException(status_code=404, detail="Livre non trouvé")

    @staticmethod
    def delete_book(book_id: int):
        for book in books:
            if book.id == book_id:
                books.remove(book)
                return
        raise HTTPException(status_code=404, detail="Livre non trouvé")
