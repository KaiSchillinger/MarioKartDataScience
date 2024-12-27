from database.base import SessionLocal
from database.models import Data

session = SessionLocal()

# Beispiel für eine Abfrage
entries = session.query(Data).all()
for entry in entries:
    print(entry.user, entry.place)
