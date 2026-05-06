from fastapi import FastAPI
from app.routers.books import books_router
from contextlib import asynccontextmanager
from app.data.db import init_database

@asynccontextmanager
async def lifespan(app: FastAPI): #definisce operazioni da eseguire in avvio e in chiusura
    #on create
    init_database()  # Inizializza il database all'avvio dell'applicazione
    yield  # alla prima chiamata esegue fino a yield, alla seconda chiamata esegue tutto ciò che è dopo yield
    #on close

app = FastAPI(lifespan=lifespan)
app.include_router(books_router) # includiamo il router dei libri nell'app principale