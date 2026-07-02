from pydantic import BaseModel


class WorkspaceCreate(BaseModel):  # type: ignore[misc]
    """Схема для создания воркспейса."""

    name: str
    owner_id: str


class WorkspaceRead(BaseModel):  # type: ignore[misc]
    """Схема для чтения воркспейса."""

    id: str
    name: str
    owner_id: str

    model_config = {"from_attributes": True}
