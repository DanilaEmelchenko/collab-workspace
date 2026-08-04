from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):  # type: ignore[misc]
    title: str = Field(min_length=1, max_length=255)
    workspace_id: str | None = None


class DocumentRead(BaseModel):  # type: ignore[misc]
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    workspace_id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None
