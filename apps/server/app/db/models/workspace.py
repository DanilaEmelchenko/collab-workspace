from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import BaseModel


class Workspace(BaseModel):
    __tablename__ = "workspaces"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    owner_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    # Отношения (не загружаются по умолчанию, нужны для ORM)
    owner = relationship("User", back_populates="workspaces")
    documents = relationship("Document", back_populates="workspace", cascade="all, delete-orphan")
