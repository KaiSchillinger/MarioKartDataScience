from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Controller(Base):
    __tablename__ = 'controller'

    id: Mapped[Base.primary_key_int]
    controller: Mapped[Base.str_50] = mapped_column(nullable=False)

    data: Mapped[list["Data"]] = relationship(back_populates="controller")
