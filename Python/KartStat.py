import streamlit as st
import pandas as pd
import os

# Dateiname für den Datensatz
DATAFILE = '../CSV/KartStats.csv'

# Funktion, um den Datensatz zu laden oder zu erstellen
def load_data():
    if os.path.exists(DATAFILE):
        return pd.read_csv(DATAFILE)
    else:
        # Leerer DataFrame mit den angegebenen Spalten
        return pd.DataFrame(columns=["id", "spieler", "platzierung", "controller", "strecken",
                                      "drink_count", "kiff_count", "datum", "rennen_tag",
                                      "gesamt_score", "beamer", "fehlstarts"])

# Funktion, um den Datensatz zu speichern
def save_data(data):
    data.to_csv(DATAFILE, index=False)

# Hauptfunktion der Streamlit-App
def main():
    st.title("Statistik Dateneingabe")

    # Lade vorhandene Daten
    data = load_data()

    # ID für den nächsten Eintrag generieren
    next_id = data['id'].max() + 1 if not data.empty else 1

    # Benutzeroberfläche für die Dateneingabe
    st.header("Neue Daten eingeben")

    spieler = st.text_input("Spieler")
    platzierung = st.number_input("Platzierung", min_value=1)
    controller = st.text_input("Controller")
    strecken = st.text_input("Strecken")
    drink_count = st.number_input("Drink Count", min_value=0)
    kiff_count = st.number_input("Kiff Count", min_value=0)
    datum = st.date_input("Datum")
    rennen_tag = st.text_input("Rennentag")
    gesamt_score = st.number_input("Gesamt Score", min_value=0)
    beamer = st.number_input("Beamer", min_value=0)
    fehlstarts = st.number_input("Fehlstarts", min_value=0)

    if st.button("Daten hinzufügen"):
        # Neue Daten zur Tabelle hinzufügen
        new_data = pd.DataFrame([[next_id, spieler, platzierung, controller, strecken,
                                   drink_count, kiff_count, datum, rennen_tag,
                                   gesamt_score, beamer, fehlstarts]],
                                columns=["id", "spieler", "platzierung", "controller",
                                         "strecken", "drink_count", "kiff_count",
                                         "datum", "rennen_tag", "gesamt_score",
                                         "beamer", "fehlstarts"])
        data = pd.concat([data, new_data], ignore_index=True)
        save_data(data)
        st.success("Daten erfolgreich hinzugefügt!")

    # Anzeigen der aktuellen Daten
    st.header("Aktuelle Daten")
    st.dataframe(data)

if __name__ == "__main__":
    main()
