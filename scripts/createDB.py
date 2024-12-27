import pandas as pd
import logging
from database.base import Base, engine, SessionLocal
from database.models import *

# Logging konfigurieren
logging.basicConfig(
    filename="logs/CreateDB.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Tabellen erstellen, falls sie nicht existieren
Base.metadata.create_all(bind=engine)

# CSV-Datei laden
df_scores = pd.read_csv("../data/scores.csv", sep=';')
df_tracks = pd.read_csv("../data/tracks.csv", sep=';')
df_user = pd.read_csv("../data/user.csv", sep=';')
df_controller = pd.read_csv("../data/controller.csv", sep=';')

# scores.csv-Daten in die Datenbank schreiben
try:
    with SessionLocal() as session:
        for index, row in df_scores.iterrows():
            scores = Scores(
                place=int(row['place']),
                points=int(row['points'])
            )
            session.add(scores)
        session.commit()
        print("Scores erfolgreich in die Tabelle eingefügt.")

        for index, row in df_tracks.iterrows():
            tracks = Tracks(
                cup_de=str(row['cup_de']),
                cup_en=str(row['cup_en']),
                track_de=str(row['track_de']),
                track_en=str(row['track_en']),
                game=str(row['game'])
            )
            session.add(tracks)
        session.commit()
        print("Tracks erfolgreich in die Tabelle eingefügt.")

        for index, row in df_controller.iterrows():
            controller = Controller(
                controller=str(row['controller'])
            )
            session.add(controller)
        session.commit()
        print("Controller erfolgreich in die Tabelle eingefügt.")

        for index, row in df_user.iterrows():
            user = User(
                name=str(row['name'])
            )
            session.add(user)
        session.commit()
        print("User erfolgreich in die Tabelle eingefügt.")

except Exception as e:
    logging.error(f"Fehler befüllen der Spalte der Datenbank: {e}")
    print(f"Fehler beim Einfügen der Daten: {e}")
