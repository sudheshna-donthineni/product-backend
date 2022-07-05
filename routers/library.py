from fastapi import APIRouter
from database import db
import secrets
import string
from models.library import BookItem, TransactionItem
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/library")


@router.get("/get-all-books")
async def get_all_books():
    """Retrieves all books"""

    docs = db.collection("library").stream()
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    return data


@router.get("/create-book-id")
async def create_book_id():
    """Creates a book ID"""

    book_id = "".join(
        [secrets.choice(string.ascii_letters + string.digits) for _ in range(8)]
    )

    result = db.collection("library").where("bookId", "==", book_id).get()

    if not result:
        return book_id


@router.post("/create-book", status_code=201)
async def create_book(book: BookItem):
    """Creates a new book"""

    json_book = jsonable_encoder(book)
    json_book["status"] = "Available"
    result = db.collection("library").document().set(json_book)
    print(result)
    return


@router.post("/create-transaction", status_code=201)
async def create_transaction(transaction: TransactionItem):
    """Creates a new library transaction"""

    json_transaction = jsonable_encoder(transaction)
    result = db.collection("library-transactions").document().set(json_transaction)
    print(result)
    return


@router.get("/get-transaction-by-book/")
async def get_transaction_by_book(book_id: str):
    """Retrieves transaction details by book ID"""

    docs = (
        db.collection("library-transactions").where("book_id", "==", book_id).stream()
    )
    data = []
    for doc in docs:
        doc.to_dict()["borrowed_date"] = doc.to_dict()["borrowed_date"].split("T")[0]
        print(doc.to_dict())
        data.append(doc.to_dict())
    return data
