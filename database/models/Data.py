from datetime import datetime

from sqlalchemy import Integer, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Data(Base):
    __tablename__ = 'data'

    id: Mapped[Base.primary_key_int]
    user: Mapped[Base.str_50]
    places_id: Mapped[Base.place_fk]
    controller_id: Mapped[Base.controller_fk]
    tracks_id: Mapped[Base.tracks_fk]
    drink_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    kiff_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    datum: Mapped[datetime] = mapped_column(TIMESTAMP)
    rennen_tag: Mapped[int] = mapped_column(Integer, nullable=False)
    gesamt_score: Mapped[int] = mapped_column(Integer, nullable=False)
    beamer: Mapped[bool] = mapped_column(default=True)
    fehlstarts: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Definiere die Beziehungen zu Score und Strecken
    gameplace: Mapped["GamePlace"] = relationship(back_populates="data")
    gametracks: Mapped["GameTracks"] = relationship(back_populates="data")
    controller: Mapped["Controller"] = relationship(back_populates="data")
