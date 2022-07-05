from datetime import datetime
from pydantic import BaseModel


class BookItem(BaseModel):
    id: str
    title: str
    author: str
    genre: str
    number_of_pages: int


class TransactionItem(BaseModel):
    student_id: str
    student_name: str
    borrowed_date: datetime
    issuer: str
    book_id: str
    book_title: str
