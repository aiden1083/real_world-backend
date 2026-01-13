from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from .article_model import Article

class User(Base):
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    bio: Mapped[str] = mapped_column(String(1000), default="", nullable=False)
    image: Mapped[str] = mapped_column(String(1000), default="", nullable=False)

    favorites: Mapped[list["Article"]] = relationship(
        "Article",
        secondary="users_articles",
        back_populates="favorited_by",
        lazy="selectin"
    )
