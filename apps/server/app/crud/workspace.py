import uuid
from typing import cast

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.workspace import Workspace
from app.schemas.workspace import WorkspaceCreate


async def create_workspace(db: AsyncSession, workspace_in: WorkspaceCreate) -> Workspace:
    """Создать новый воркспейс."""
    workspace = Workspace(
        name=workspace_in.name,
        owner_id=uuid.UUID(workspace_in.owner_id),
    )
    db.add(workspace)
    await db.commit()
    await db.refresh(workspace)
    return cast(Workspace, workspace)


async def get_workspaces(db: AsyncSession) -> list[Workspace]:
    """Получить список всех воркспейсов."""
    stmt = select(Workspace)
    result = await db.execute(stmt)
    return cast(list[Workspace], list(result.scalars().all()))


async def get_workspace(db: AsyncSession, workspace_id: str) -> Workspace | None:
    """Получить воркспейс по ID."""
    try:
        workspace_uuid = uuid.UUID(workspace_id)
    except ValueError:
        return None
    return cast(Workspace | None, await db.get(Workspace, workspace_uuid))


async def get_or_create_personal_workspace(db: AsyncSession, owner_id: str) -> Workspace:
    """Личный воркспейс пользователя: найти или создать."""
    stmt = select(Workspace).where(Workspace.owner_id == uuid.UUID(owner_id)).limit(1)
    result = await db.execute(stmt)
    workspace = result.scalar_one_or_none()
    if workspace is not None:
        return cast(Workspace, workspace)

    workspace = Workspace(name="Личное пространство", owner_id=uuid.UUID(owner_id))
    db.add(workspace)
    await db.commit()
    await db.refresh(workspace)
    return cast(Workspace, workspace)
