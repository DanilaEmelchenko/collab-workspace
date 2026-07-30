from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import decode_access_token
from app.crud.user import create_user, get_user, get_user_by_email
from app.db.session import get_session
from app.schemas.user import UserCreate, UserRead

router = APIRouter()


@router.post("/", response_model=UserRead, status_code=201)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_session)) -> UserRead:
    """Регистрация нового пользователя."""
    try:
        return await create_user(db, user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None


@router.get("/me", response_model=UserRead)
async def read_current_user(
    authorization: str = Header(None), db: AsyncSession = Depends(get_session)
) -> UserRead:
    """Получение текущего пользователя."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Требуется авторизация")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Неверный формат авторизации")

    token = authorization.replace("Bearer ", "")

    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Неверный токен")

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Неверный токен")

    # Пробуем найти по ID
    user = await get_user(db, user_id)

    # Если не нашли - пробуем по email
    if user is None:
        user = await get_user_by_email(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return user


@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: str, db: AsyncSession = Depends(get_session)) -> UserRead:
    """Получение пользователя по ID."""
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user
