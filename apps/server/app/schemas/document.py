from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):  # type: ignore[misc]
    """Схема создания документа."""

    title: str = Field(min_length=1, max_length=255)
    workspace_id: str | None = None  # если не указан — личный воркспейс


class DocumentRead(BaseModel):  # type: ignore[misc]
    """Схема чтения документа."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    workspace_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
