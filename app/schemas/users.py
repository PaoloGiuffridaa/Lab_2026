from sqlmodel import SQLModel, Field
from datetime import date

class UserBase(SQLModel):
    name: str
    birth_date: date 
    city: str

class UserDB(UserBase, table=True):
    id: int = Field(default=None, primary_key=True) #id univoco
    password: str = Field(default="password") #password di default per tutti gli utenti

class UserPublic(UserBase):
    pass
