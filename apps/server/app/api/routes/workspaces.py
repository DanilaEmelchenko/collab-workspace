from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.workspace import create_workspace, get_workspaces
from app.db.session import get_session
from app.schemas.workspace import WorkspaceCreate, WorkspaceRead

router = APIRouter()


@router.post("/", response_model=WorkspaceRead, status_code=201)
async def create_new_workspace(
    workspace_in: WorkspaceCreate, db: AsyncSession = Depends(get_session)
) -> WorkspaceRead:
    """Создание нового воркспейса."""
    return await create_workspace(db, workspace_in)


@router.get("/", response_model=list[WorkspaceRead])
async def list_workspaces(db: AsyncSession = Depends(get_session)) -> list[WorkspaceRead]:
    """Получение списка воркспейсов."""
    return await get_workspaces(db)
