from sqlmodel import SQLModel, Field

class BookUserLink(SQLModel, table=True):
    book_id: int = Field(default=None, foreign_key="bookdb.id", primary_key=True)
    user_id: int = Field(default=None, foreign_key="userdb.id", primary_key=True)