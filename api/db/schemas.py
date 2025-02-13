from enum import Enum
from typing import OrderedDict
from pydantic import BaseModel

class Genre(str, Enum):
    SCI_FI = "Science Fiction"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    THRILLER = "Thriller"

class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    genre: Genre

class InMemoryDB:
    def __init__(self):
        self.books: OrderedDict[int, Book] = {}

    def get_books(self) -> OrderedDict[int, Book]:
        return self.books

    def add_book(self, book: Book) -> Book:
        self.books.update({book.id: book})
        return book

    def get_book(self, book_id: int) -> Book:
        return self.books.get(book_id)

    def update_book(self, book_id: int, data: Book) -> Book:
        self.books.update({book_id: data})
        return self.books.get(book_id)

    def delete_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]

# Create an instance of the InMemoryDB
books = InMemoryDB()
