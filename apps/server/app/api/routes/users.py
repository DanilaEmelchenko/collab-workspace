from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user import create_user, get_user
from app.db.session import get_session
from app.schemas.user import UserCreate, UserRead

router = APIRouter()


@router.post("/", response_model=UserRead, status_code=201)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_session)) -> UserRead:
    """Регистрация нового пользователя."""
    return await create_user(db, user_in)


@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: str, db: AsyncSession = Depends(get_session)) -> UserRead:
    """Получение пользователя по ID."""
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user
