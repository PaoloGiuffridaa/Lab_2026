from fastapi import APIRouter, Path, HTTPException
from app.schemas.book import BookCreate, BookPublic, BookDB, Book
from app.schemas.review import Review
from typing import Annotated    #aggiunge alla tipizzazione degli altri metadati
from app.data.db import SessionDep
from sqlmodel import select, delete

books_router = APIRouter(prefix="/books", tags=["books"]) # tutte le rotte che iniziano con /books saranno in questo router, e avranno il tag "books" per la documentazione

@books_router.get("/")
def get_all_books(
    session : SessionDep,    #aggiungiamo la dipendenza per la sessione del database
    sort: Annotated[bool, Path(description="Sort the book by review", example="True")] = False,
) -> list[BookPublic]:    # pydantic fa la validazione dell'output, se non è un dict, FastAPI restituirà un errore    
    """
    Return the list of all books
    """
    books = session.exec(select(BookDB)).all() #recupera tutti i libri dal database
    if sort:
        sorted(books, key=lambda book: book.review) #non è typing è sintassi lambda func
    return list(books)



#API per ottenere un libro specifico tramite il suo ID
@books_router.get("/{book_id}")
def get_book_by_id(
    session : SessionDep,    #aggiungiamo la dipendenza per la sessione del database
    book_id: Annotated[int, Path(description="The ID of the book to retrieve", example=0)]  #aggiungiamo la descrizione del parametro
    ) -> BookPublic:
    """
    Return a book by its ID
    """
    book = session.get(BookDB, book_id) #get da tabella il valore della PK

    #in teoria la funzione restituisce un BookPublic ma la session restituisce un BookDB, 
    # #FastAPI si occuperà di convertire il modello in BookPublic essendo compatibili
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")
    
#API per aggiornare la recensione di un libro
@books_router.post("/{book_id}/review")
def update_book_review(
    session : SessionDep,    #aggiungiamo la dipendenza per la sessione del database
    book_id: Annotated[int, Path(description="The ID of the book to update", example=0)],
    review: Review  #FastApi andrà a recuperare il valore del parametro review dal body della richiesta
    ):
    """
    Update the review of a book by its ID
    """
    book = session.get(BookDB, book_id) #recupera il libro dal database
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.review = review.rating #aggiorna la recensione del libro
    session.add(book) #aggiunge il libro alla sessione del database
    session.commit() #salva le modifiche al database
    return "Book review updated successfully"
    
@books_router.post("/")
def add_book(
    session: SessionDep,
    book: BookCreate
):
    """Add a new book to the collection"""
    book_entry = BookDB.model_validate(book) #converte il modello/JSON di input in un modello compatibile con la tabella del database    
    session.add(book_entry) #aggiunge il libro alla sessione del database
    session.commit() #salva le modifiche al database
    return "Book added successfully"

@books_router.put("/{book_id}")
def replace_book(
    session: SessionDep,
    id: Annotated[int, Path(description="The ID of the book to replace", example=0)],
    book: Book):    
    """Replace an existing book with a new one"""
    existing_book = session.get(BookDB, id) #recupera il libro esistente dal database
    if not existing_book:   #se il libro non esiste, restituisce un errore 404
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = existing_book.title #mantiene il titolo del libro esistente
    book.author = existing_book.author #mantiene l'autore del libro esistente
    book.review = existing_book.review #mantiene la recensione del libro esistente
    session.add(book) #aggiunge il nuovo libro alla sessione del database
    session.commit() #salva le modifiche al database
    return "Book replaced successfully"

@books_router.delete("/")
def delete_all_books(session: SessionDep):
    """Delete all books from the collection"""
    session.exec(delete(BookDB)) #esegue una query di delete per eliminare tutti i libri
    session.commit() #salva le modifiche al database
    return "All books deleted successfully"

@books_router.delete("/{book_id}")
def delete_book(
    session: SessionDep,
    book_id: Annotated[int, Path(description="The ID of the book to delete", example=0)]
):
    """Delete a book from the collection"""
    session.exec(delete(BookDB).where(BookDB.id == book_id)) #esegue una query di delete per eliminare il libro con l'ID specificato
    session.commit()
    return "Book deleted successfully"
