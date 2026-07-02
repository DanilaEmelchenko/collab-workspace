from pydantic import BaseModel


class UserCreate(BaseModel):  # type: ignore[misc]
    """Схема для создания пользователя (входящие данные)."""

    email: str
    password: str


class UserRead(BaseModel):  # type: ignore[misc]
    """Схема для чтения пользователя (исходящие данные)."""

    id: str
    email: str
    is_active: bool

    # Позволяет Pydantic автоматически конвертировать ORM-объект SQLAlchemy в JSON
    model_config = {"from_attributes": True}
