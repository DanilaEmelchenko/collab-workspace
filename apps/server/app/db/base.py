import uuid
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):  # type: ignore[misc]
    """Базовый класс для всех моделей."""

    pass


class TimestampMixin:
    """Mixin для добавления полей времени создания и обновления."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )


class BaseModel(TimestampMixin, Base):
    """Базовая модель с UUID первичным ключом и временными метками."""

    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4, index=True)
