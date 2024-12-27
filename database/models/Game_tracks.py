from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class GameTracks(Base):
    __tablename__ = 'game_tracks'

    id: Mapped[Base.primary_key_int]
    track_1: Mapped[int] = mapped_column(Integer)
    track_2: Mapped[int] = mapped_column(Integer)
    track_3: Mapped[int] = mapped_column(Integer)
    track_4: Mapped[int] = mapped_column(Integer)

    data: Mapped[list["Data"]] = relationship(back_populates="gametracks")
