import streamlit as st
import pandas as pd
import os
import datetime

# Dateiname für den Datensatz
DATAFILE = 'data.csv'
df_strecken = pd.read_csv('../Zusatzdaten/strecken_cups.csv')
streckenauswahl = df_strecken['Strecke'].tolist()
controller_options = ["Pro", "Plus Rot", "Plus Gelb", "Minus Blau", "Minus Gelb"]

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

    # Session State für den Fortschritt und die Datenverwaltung initialisieren
    if "step" not in st.session_state:
        st.session_state.step = 1  # Step 1: Abfrage der Spieleranzahl
        st.session_state.player_count = 0
        st.session_state.players = []
        st.session_state.current_player_index = 0

    # ID für den nächsten Eintrag generieren
    next_id = int(data['id'].max()) + 1 if not data.empty else 1

    # Step 1: Spieleranzahl abfragen
    if st.session_state.step == 1:
        st.header("Anzahl der Spieler eingeben")
        player_count = st.number_input("Anzahl der Spieler", min_value=1, step=1)

        if st.button("Weiter"):
            st.session_state.player_count = player_count
            st.session_state.step = 2  # Weiter zu Schritt 2

    # Step 2: Namen der Spieler abfragen
    elif st.session_state.step == 2:
        st.header("Namen der Spieler eingeben")
        st.session_state.players = []

        for i in range(st.session_state.player_count):
            player_name = st.text_input(f"Spieler {i + 1} Name")
            st.session_state.players.append(player_name)

        if st.button("Weiter zu Dateneingabe"):
            st.session_state.step = 3  # Weiter zu Schritt 3

    # Step 3: Dateneingabe für jeden Spieler
    elif st.session_state.step == 3:
        current_player = st.session_state.players[st.session_state.current_player_index]
        st.header(f"Daten für Spieler: {current_player}")

        datum = st.date_input("Datum", value=datetime.date.today())
        controller = st.selectbox("Controller", controller_options)

        # Boolean für Beamer (Ja/Nein)
        beamer = st.checkbox("Beamer")

        # Zwei Spalten für Platzierungen und Strecken nebeneinander
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Strecken")
            strecken_options = streckenauswahl
            strecke_1 = st.selectbox("Strecke 1", strecken_options)
            strecke_2 = st.selectbox("Strecke 2", strecken_options, index=1)
            strecke_3 = st.selectbox("Strecke 3", strecken_options, index=2)
            strecke_4 = st.selectbox("Strecke 4", strecken_options, index=3)
            strecken = [strecke_1, strecke_2, strecke_3, strecke_4]

        with col2:
            st.subheader("Platzierungen")
            platzierung_1 = st.number_input("Platzierung 1", min_value=1)
            platzierung_2 = st.number_input("Platzierung 2", min_value=1)
            platzierung_3 = st.number_input("Platzierung 3", min_value=1)
            platzierung_4 = st.number_input("Platzierung 4", min_value=1)
            platzierung = [platzierung_1, platzierung_2, platzierung_3, platzierung_4]

        # Weitere Eingabefelder
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Drinks")
            drink_count = st.number_input("Drink Count", min_value=0)

        with col4:
            st.subheader("Kiffs")
            kiff_count = st.number_input("Kiff Count", min_value=0)

        # Weitere Eingabefelder
        col5, col6, col7 = st.columns(3)

        with col5:
            rennen_tag = st.number_input("Rennentag", min_value=0)
        with col6:
            gesamt_score = st.number_input("Gesamt Score", min_value=0)
        with col7:
            fehlstarts = st.number_input("Fehlstarts", min_value=0)

        if st.button("Daten für Spieler hinzufügen"):
            # Neue Daten zur Tabelle hinzufügen
            new_data = pd.DataFrame([[next_id, current_player, platzierung, controller, strecken,
                                      drink_count, kiff_count, datum, rennen_tag,
                                      gesamt_score, beamer, fehlstarts]],
                                    columns=["id", "spieler", "platzierung", "controller",
                                             "strecken", "drink_count", "kiff_count",
                                             "datum", "rennen_tag", "gesamt_score",
                                             "beamer", "fehlstarts"])
            data = pd.concat([data, new_data], ignore_index=True)
            save_data(data)
            st.success(f"Daten für {current_player} hinzugefügt!")

            # Zum nächsten Spieler wechseln oder zurück zum Start
            st.session_state.current_player_index += 1
            if st.session_state.current_player_index >= st.session_state.player_count:
                st.session_state.step = 1  # Zurück zu Schritt 1
                st.session_state.current_player_index = 0
                st.session_state.players = []  # Spieler-Liste zurücksetzen
            else:
                next_id += 1  # Nächste ID für den neuen Eintrag erhöhen

    # Anzeigen der aktuellen Daten
    st.header("Aktuelle Daten")
    st.dataframe(data)


if __name__ == "__main__":
    main()
