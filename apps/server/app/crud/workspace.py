from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.workspace import Workspace
from app.schemas.workspace import WorkspaceCreate


async def get_workspaces(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Workspace]:
    """Получить список воркспейсов."""
    from sqlalchemy import select

    result = await db.execute(select(Workspace).offset(skip).limit(limit))
    return list(result.scalars().all())


async def create_workspace(db: AsyncSession, workspace_in: WorkspaceCreate) -> Workspace:
    """Создать новый воркспейс."""
    db_workspace = Workspace(name=workspace_in.name, owner_id=workspace_in.owner_id)
    db.add(db_workspace)
    await db.commit()
    await db.refresh(db_workspace)
    return db_workspace
