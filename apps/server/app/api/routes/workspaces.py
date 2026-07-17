from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.crud.workspace import create_workspace, get_workspaces
from app.db.models.user import User
from app.db.session import get_session
from app.schemas.workspace import WorkspaceCreate, WorkspaceRead

router = APIRouter()


@router.post("/", response_model=WorkspaceRead, status_code=201)
async def create_new_workspace(
    workspace_in: WorkspaceCreate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),  # <-- Защита
) -> WorkspaceRead:
    workspace_in.owner_id = str(current_user.id)
    return await create_workspace(db, workspace_in)


@router.get("/", response_model=list[WorkspaceRead])
async def list_workspaces(
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),  # <-- Защита
) -> list[WorkspaceRead]:
    return await get_workspaces(db)
