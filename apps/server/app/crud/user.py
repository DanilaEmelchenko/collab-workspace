import uuid
from typing import cast

import bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user import User
from app.schemas.user import UserCreate


async def get_user(db: AsyncSession, user_id: str) -> User | None:
    """Получить пользователя по ID."""
    try:
        user_uuid = uuid.UUID(user_id)
    except ValueError:
        return None
    result = await db.get(User, user_uuid)
    return cast(User | None, result)


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    """Создать нового пользователя."""
    password_bytes = user_in.password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    db_user = User(email=user_in.email, hashed_password=hashed_password.decode("utf-8"))
    db.add(db_user)

    try:
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except IntegrityError:
        await db.rollback()
        raise ValueError("Пользователь с таким email уже существует") from None
