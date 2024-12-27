import os
from database.base import Base, engine
import logging

# Logging konfigurieren (für Tests separat)
logging.basicConfig(
    filename="test.log",  # Separate Log-Datei für Tests
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def test_database_creation():
    """
    Testet, ob die Tabellen in der Datenbank erfolgreich erstellt werden können.
    """
    try:
        Base.metadata.create_all(bind=engine)
        assert os.path.exists("DB_Test.db"), "Datenbankdatei wurde nicht erstellt."
        logging.info("Test erfolgreich: Datenbank und Tabellen wurden erstellt.")
    except Exception as e:
        logging.error(f"Test fehlgeschlagen: {e}")
        assert False, f"Fehler beim Erstellen der Datenbank: {e}"
