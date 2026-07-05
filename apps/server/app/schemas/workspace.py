from uuid import UUID

from pydantic import BaseModel


class WorkspaceCreate(BaseModel):  # type: ignore[misc]
    """Схема для создания воркспейса."""

    name: str
    owner_id: str


class WorkspaceRead(BaseModel):  # type: ignore[misc]
    """Схема для чтения воркспейса."""

    id: UUID
    name: str
    owner_id: UUID

    model_config = {"from_attributes": True}
