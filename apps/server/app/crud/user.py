import uuid
from typing import cast

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash, verify_password
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


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    """Получить пользователя по email."""
    from sqlalchemy import select

    result = await db.execute(select(User).where(User.email == email))
    return cast(User | None, result.scalar_one_or_none())


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    """Создать нового пользователя."""
    db_user = User(email=user_in.email, hashed_password=get_password_hash(user_in.password))
    db.add(db_user)

    try:
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except IntegrityError:
        await db.rollback()
        raise ValueError("Пользователь с таким email уже существует") from None


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User | None:
    """Аутентифицирует пользователя по email и паролю."""
    user = await get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
