from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class GamePlace(Base):
    __tablename__ = 'game_place'

    id: Mapped[Base.primary_key_int]
    place_1: Mapped[int] = mapped_column(Integer)
    place_2: Mapped[int] = mapped_column(Integer)
    place_3: Mapped[int] = mapped_column(Integer)
    place_4: Mapped[int] = mapped_column(Integer)

    data: Mapped[list["Data"]] = relationship(back_populates="gameplace")
