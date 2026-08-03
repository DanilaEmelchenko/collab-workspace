import uuid
from typing import cast

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.document import Document
from app.db.models.workspace import Workspace


async def get_documents_for_user(db: AsyncSession, user_id: str) -> list[Document]:
    """Все документы из воркспейсов, которыми владеет пользователь."""
    stmt = (
        select(Document)
        .join(Workspace, Document.workspace_id == Workspace.id)
        .where(Workspace.owner_id == uuid.UUID(user_id))
        .order_by(Document.id)
    )
    result = await db.execute(stmt)
    return cast(list[Document], list(result.scalars().all()))


async def create_document(db: AsyncSession, title: str, workspace_id: str) -> Document:
    """Создать документ в воркспейсе."""
    document = Document(
        title=title,
        workspace_id=uuid.UUID(workspace_id),
    )
    db.add(document)
    await db.commit()
    await db.refresh(document)
    return cast(Document, document)


async def get_document(db: AsyncSession, document_id: str) -> Document | None:
    """Получить документ по ID."""
    try:
        doc_uuid = uuid.UUID(document_id)
    except ValueError:
        return None
    result = await db.get(Document, doc_uuid)
    return cast(Document | None, result)
