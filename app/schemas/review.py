from pydantic import BaseModel, Field
from typing import Annotated    #aggiunge alla tipizzazione degli altri metadati

class Review(BaseModel):
    review: Annotated[int, Field(ge=1, le=5, examples=[2])] #valore obbligatorio, deve essere compreso tra 1 e 5

    
