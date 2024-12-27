from datetime import datetime
from typing_extensions import Annotated

from sqlalchemy import create_engine, String, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped, DeclarativeBase, Session

# creating database-engine
db_folder = "../data"
DATABASE_URL = f"sqlite:///{db_folder}/DB_Test.db"
engine = create_engine(DATABASE_URL, echo=True)

# SessionFactory erstellen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base-Class for ORM-Classes
class Base(DeclarativeBase):
    # Type definitions
    primary_key_int = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]
    place_fk = Annotated[int, mapped_column(ForeignKey('game_place.id'), nullable=False)]
    controller_fk = Annotated[int, mapped_column(ForeignKey('controller.id'), nullable=False)]
    tracks_fk = Annotated[int, mapped_column(ForeignKey('game_tracks.id'), nullable=False)]
    str_50 = Annotated[str, mapped_column(String(50))]

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    @classmethod
    def get_by_id(cls, session, record_id):
        return session.query(cls).filter(cls.id == record_id).first()

    def save(self,session: Session):
        session.add(self)
        session.commit()


class Updated:
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())