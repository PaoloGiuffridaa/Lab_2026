from fastapi import APIRouter, HTTPException
from app.data.db import SessionDep
from app.schemas.book_user_link import BookUserLink
from app.schemas.users import UserDB, UserPublic
from app.schemas.book import BookDB, BookPublic
from sqlmodel import select

users_router = APIRouter(prefix="/users")

@users_router.get("/")
def get_all_users(session: SessionDep) -> list[UserPublic]:
    """return all users"""
    users = session.exec(select(UserDB)).all()
    return users

@users_router.get("/{user_id}/books")
def get_user_by_id(user_id: int, session: SessionDep) -> list[BookPublic]:
    """return all books of a user"""
    user = session.get(UserDB, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    statement = select(BookDB).join(BookUserLink).where(BookUserLink.user_id == user_id) #join tra le tabelle BookDB e BookUserLink, filtrando per user_id
    books = session.exec(statement).all()
    return books


