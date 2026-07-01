from sqlalchemy import ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[bytes | None] = mapped_column(
        LargeBinary, nullable=True
    )  # Для бинарных данных Yjs
    workspace_id: Mapped[str] = mapped_column(
        ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
    )

    workspace = relationship("Workspace", back_populates="documents")
