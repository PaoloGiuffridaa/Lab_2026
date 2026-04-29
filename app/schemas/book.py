from pydantic import BaseModel, Field
from typing import Annotated    #aggiunge alla tipizzazione degli altri metadati

class Book(BaseModel):
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
    1: Book(id=1, title="Il Maestro e Margherita", author="Michail Bulgakov", review=5),
    2: Book(id=2, title="Il Signore degli Anelli", author="J.R.R. Tolkien", review=5)
}



    

