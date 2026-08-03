from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.crud.document import create_document, get_document, get_documents_for_user
from app.crud.workspace import get_or_create_personal_workspace, get_workspace
from app.db.models.user import User
from app.db.session import get_session
from app.schemas.document import DocumentCreate, DocumentRead

router = APIRouter()


@router.get("/me", response_model=list[DocumentRead])
async def list_my_documents(
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
) -> list[DocumentRead]:
    """Список документов текущего пользователя."""
    return await get_documents_for_user(db, str(current_user.id))


@router.post("/", response_model=DocumentRead, status_code=201)
async def create_new_document(
    document_in: DocumentCreate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
) -> DocumentRead:
    """Создание документа (по умолчанию — в личном воркспейсе)."""
    if document_in.workspace_id is not None:
        workspace = await get_workspace(db, document_in.workspace_id)
        if workspace is None or str(workspace.owner_id) != str(current_user.id):
            raise HTTPException(status_code=403, detail="Нет доступа к этому воркспейсу")
    else:
        workspace = await get_or_create_personal_workspace(db, str(current_user.id))

    return await create_document(db, document_in.title, str(workspace.id))


@router.get("/{document_id}", response_model=DocumentRead)
async def read_document(
    document_id: str,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
) -> DocumentRead:
    """Получение документа по ID (только для владельца)."""
    document = await get_document(db, document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Документ не найден")

    workspace = await get_workspace(db, str(document.workspace_id))
    if workspace is None or str(workspace.owner_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Документ не найден")

    return document
