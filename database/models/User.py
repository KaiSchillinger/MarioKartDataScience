from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[Base.primary_key_int]
    name: Mapped[Base.str_50] = mapped_column(unique=True)
