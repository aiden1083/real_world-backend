from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.db.base import Base

class Tag(Base):
    __tablename__ = "tags"

