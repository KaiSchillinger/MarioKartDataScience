from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import User


def add_user(session: Session, user_name: str) -> bool:
    """
    Fügt einen neuen Benutzer in die Tabelle `user` ein.

    Args:
        session (Session): Die SQLAlchemy-Datenbanksitzung.
        user_name (str): Der Name des Benutzers, der hinzugefügt werden soll.

    Returns:
        bool: True, wenn der Benutzer erfolgreich hinzugefügt wurde, False bei einem Fehler.
    """
    try:
        # Neuen Benutzer erstellen
        new_user = User(name=user_name)

        # Benutzer zur Sitzung hinzufügen
        session.add(new_user)

        # Änderungen speichern
        session.commit()
        print(f"Benutzer '{user_name}' erfolgreich hinzugefügt.")
        return True
    except IntegrityError:
        # Rollback, falls ein Fehler auftritt (z.B. Name ist nicht eindeutig)
        session.rollback()
        print(f"Fehler: Benutzer '{user_name}' konnte nicht hinzugefügt werden (Name bereits vergeben).")
        return False
    except Exception as e:
        session.rollback()
        print(f"Ein Fehler ist aufgetreten: {e}")
        return False
