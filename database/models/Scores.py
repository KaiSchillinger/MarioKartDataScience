from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class Scores(Base):
    __tablename__ = 'scores'

    place: Mapped[int] = mapped_column(Integer, primary_key=True)
    points: Mapped[int] = mapped_column(Integer)
