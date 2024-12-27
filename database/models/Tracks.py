from typing import Optional
from sqlalchemy.orm import Mapped
from database.base import Base


class Tracks(Base):
    __tablename__ = 'tracks'

    id: Mapped[Base.primary_key_int]
    cup_de: Mapped[Optional[Base.str_50]]
    cup_en: Mapped[Optional[Base.str_50]]
    track_de: Mapped[Optional[Base.str_50]]
    track_en: Mapped[Optional[Base.str_50]]
    game: Mapped[Optional[Base.str_50]]
