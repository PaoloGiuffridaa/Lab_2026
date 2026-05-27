from pydantic import BaseModel
from typing import Annotated    #aggiunge alla tipizzazione degli altri metadati
from sqlmodel import SQLModel, Field

#quando book diventa SQLmodel non implementa più la validazione dell'input di pydantic, devo farla usando altre classi
class BookBase(SQLModel):
    title: str
    author: str
    review: Annotated[int, Field(ge=1, le=5)] = None #valore di default (campo opzionale)

#classe utilizzata nelle post
class BookCreate(BookBase):
    pass

#schema usato nelle get
class BookPublic(BookBase):
    id: int

class BookDB(BookBase, table=True):#sia modello pydantic che tabella ORM 
    id: int = Field(default = None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="userdb.id")  #aggiungiamo la chiave esterna degli utenti, I NOMI DELLE TABELLE SONO I NOMI DELLE CLASSI IN MINUSCOLO

class Book(SQLModel): 
    #pydantic fa la validazione dell'input
    id: int
    title: str
    author: str
    review: Annotated[int, Field(ge=1, le=5)] = None #valore di default (campo opzionale)

    model_config  = {   # JSON che contiene tutti i metadati descritti Book.model_json_schema(), aggiungiamo example
        "json_schema_extra" : {
            "examples": [
                {
                    "id": 1,
                    "title": "Il nome della Rosa",
                    "author": "Umberto Eco",
                    "review": 5
                }
            ]
        }
    }

books = {
    0: Book(id=0, title="Il nome della rosa", author="Umberto Eco", review=5),
    1: Book(id=1, title="Il Maestro e Margherita", author="Michail Bulgakov", review=3),
    2: Book(id=2, title="Il Signore degli Anelli", author="J.R.R. Tolkien", review=1)
}



    

