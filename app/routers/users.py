from fastapi import APIRouter
from app.data.db import SessionDep
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
    statement = select(BookDB).join(UserDB).where(UserDB.id == user_id)
    books = session.exec(statement).all()
    return books
