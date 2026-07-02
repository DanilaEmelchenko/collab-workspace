from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user import User
from app.schemas.user import UserCreate

# Настраиваем хэширование паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user(db: AsyncSession, user_id: str) -> User | None:
    """Получить пользователя по ID."""
    return await db.get(User, user_id)  # type: ignore[no-any-return]


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    """Создать нового пользователя."""
    # Хэшируем пароль перед сохранением
    hashed_password = pwd_context.hash(user_in.password)

    db_user = User(email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  # Обновляем объект, чтобы получить сгенерированный ID и created_at
    return db_user
