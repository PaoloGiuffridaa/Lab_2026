from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from app.schemas.book import BookDB #noqa
from app.schemas.users import UserDB #noqa
from app.schemas.book_user_link import BookUserLink #noqa
from faker import Faker #faker è una libreria che permette di generare dati casuali in varie lingue
import os

sqlite_file_name = "/media/giuff/Windows-SSD/Users/gffpl/Lab_2026/app/data/database.db"    #posizione del file in memoria
sqlite_url = f"sqlite:///{sqlite_file_name}"    #endpoint dove viene montato a runtime
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
    echo=True
    ) #creazione del motore di connessione al database

def init_database():
    ds_exists = os.path.isfile(sqlite_file_name) #controlla se il file del database esiste già
    SQLModel.metadata.create_all(engine)    #creazione del database se non esiste già
    if not ds_exists:
        f = Faker("it_IT") #creazione di un'istanza di Faker per generare dati casuali in italiano
        with Session(engine) as session:
            for _ in range(10): #genera 10 libri casuali
                book = BookDB(
                    title=f.sentence(nb_words=4), #genera un titolo casuale con 4 parole
                    author=f.name(), #genera un nome di autore casuale
                    review=f.pyint(min_value=1, max_value=5), #genera una recensione casuale tra 1 e 5
                    user_id = f.pyint(min_value=1, max_value=10) #genera un id utente casuale tra 1 e 10 (assumendo che ci siano 10 utenti)
                )
                session.add(book) #aggiunge il libro alla sessione del database
            for _ in range(10): #genera 10 utenti casuali
                user = UserDB(
                    name=f.name(), #genera un nome di utente casuale
                    birth_date=f.date_of_birth(), #genera una data di nascita casuale
                    city=f.city() #genera una città casuale
                )
                session.add(user) #aggiunge l'utente alla sessione del database 
            session.commit() #salva tutte le modifiche al database 
            for i in range(5): #genera 5 link casuali tra libri e utenti
                link = BookUserLink(
                    book_id=f.pyint(min_value=1, max_value=10), #genera un id libro casuale tra 1 e 10 (assumendo che ci siano 10 libri)
                    user_id=f.pyint(min_value=1, max_value=10) #genera un id utente casuale tra 1 e 10 (assumendo che ci siano 10 utenti)
                )
                session.add(link) #aggiunge il link alla sessione del database 
            session.commit() #salva tutte le modifiche al database 


def get_session():
    with Session(engine) as session:
        yield session   #yield permette di "bloccare" la funzione e restituire sempre la stessa istanza

#se aggiungo questo in ogni endpoint avrò la sessione se necessario --> session : SessionDep
SessionDep = Annotated[Session, Depends(get_session)] 
