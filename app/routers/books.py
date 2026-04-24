from fastapi import APIRouter, Path, HTTPException
from app.schemas.book import Book, books
from app.schemas.review import Review
from typing import Annotated    #aggiunge alla tipizzazione degli altri metadati

books_router = APIRouter(prefix="/books", tags=["books"]) # tutte le rotte che iniziano con /books saranno in questo router, e avranno il tag "books" per la documentazione

@books_router.get("/")
def get_all_books() -> list[Book]:    # pydantic fa la validazione dell'output, se non è un dict, FastAPI restituirà un errore    
    """
    Return the list of all books
    """
    return list(books.values())

#API per ottenere un libro specifico tramite il suo ID
@books_router.get("/{book_id}")
def get_book_by_id(
    book_id: Annotated[int, Path(description="The ID of the book to retrieve", example=0)]  #aggiungiamo la descrizione del parametro
    ) -> Book:
    """
    Return a book by its ID
    """
    try:
        return books[book_id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
    
#API per aggiornare la recensione di un libro
@books_router.post("/{book_id}/review")
def update_book_review(
    book_id: Annotated[int, Path(description="The ID of the book to update", example=0)],
    review: Review  #FastApi andrà a recuperare il valore del parametro review dal body della richiesta
    ):
    """
    Update the review of a book by its ID
    """
    try:
        books[book_id].review = review.review
        return "Review added successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")