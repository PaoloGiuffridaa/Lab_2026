from fastapi import FastAPI
from app.routers.books import books_router

app = FastAPI()
app.include_router(books_router) # includiamo il router dei libri nell'app principale