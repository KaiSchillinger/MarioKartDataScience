import streamlit as st
import pandas as pd
import os
import datetime

# Dateiname für den Datensatz
DATAFILE = 'data.csv'
ZIELFILE = 'data_test.csv'

# DF Strecken
df_strecken = pd.read_csv('../Zusatzdaten/strecken_cups.csv')
streckenauswahl = df_strecken['Strecke'].tolist()

# DF Scores
df_scores = pd.read_csv('../Zusatzdaten/scores.csv')
platzierungen_mapping = df_scores.set_index('platz')['punkte'].to_dict()

# Controller
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
    data.to_csv(ZIELFILE, index=False)


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
        player_count = st.number_input("Anzahl der Spieler", min_value=1, max_value=4, step=1)

        if st.button("Weiter"):
            st.session_state.player_count = player_count
            st.session_state.step = 2  # Weiter zu Schritt 2

    # Step 2: Namen der Spieler abfragen
    elif st.session_state.step == 2:

        # Datum
        datum = st.date_input("Datum", value=datetime.date.today())

        # Boolean für Beamer (Ja/Nein)
        beamer = st.checkbox("Beamer")
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.session_state.players = []

            for i in range(st.session_state.player_count):
                player_name = st.text_input(f"Spieler {i + 1} Name")
                st.session_state.players.append(player_name)

        with (col2):
            st.session_state.drinks = []

            for i in range(st.session_state.player_count):
                drink_count = st.number_input(f"Drink Count {i +1}", min_value=0)
                st.session_state.drinks.append(drink_count)

        with col3:
            st.session_state.kiffs = []

            for i in range(st.session_state.player_count):
                kiff_count = st.number_input(f"Kiff Count {i +1}", min_value=0)
                st.session_state.kiffs.append(kiff_count)

        with col4:
            st.session_state.rennen_nr = []

            for i in range(st.session_state.player_count):
                rennen_tag = st.number_input(f"Rennentag {i +1}", min_value=0)
                st.session_state.rennen_nr.append(rennen_tag)

        with col5:
            st.session_state.controller_list = []

            for i in range(st.session_state.player_count):
                controller = st.selectbox(f"Controller {i +1}", controller_options)
                st.session_state.controller_list.append(controller)

        if st.button("Weiter zu Dateneingabe"):
            st.session_state.step = 3  # Weiter zu Schritt 3

    # Step 3: Dateneingabe für jeden Spieler
    elif st.session_state.step == 3:

        # Spalten für Strecken und dynamische Spalten Platzierungen
        cols = st.columns(1 + st.session_state.player_count)

        # Streckenauswahl in der ersten Spalte
        with cols[0]:
            st.subheader("Strecke")
            strecken_options = streckenauswahl
            strecke_1 = st.selectbox("Strecke 1", strecken_options)
            strecke_2 = st.selectbox("Strecke 2", strecken_options, index=1)
            strecke_3 = st.selectbox("Strecke 3", strecken_options, index=2)
            strecke_4 = st.selectbox("Strecke 4", strecken_options, index=3)
            strecken = [strecke_1, strecke_2, strecke_3, strecke_4]

        # Dynamische Platzierungsspalten in den restlichen Spalten
        platzierungen_liste = []    # Liste zum Speichern aller Platzierungen
        gesamt_scores_liste = []    # Liste zum Speichern der Scores für jedes Platzierung-Set

        # Spalten für Platzierungen erstellen und Spielernamen als Überschriften setzen
        for idx, col in enumerate(cols[1:]):  # Ab cols[1] beginnen, da cols[0] für Strecken reserviert ist
            player_name = st.session_state.players[idx] if idx < len(st.session_state.players) else f"Spieler {idx + 1}"

            with col:
                st.subheader(player_name)  # Spielernamen als Header anzeigen
                platzierung_1 = st.number_input(f"Platzierung 1 ({player_name})", min_value=1, max_value=12, step=1)
                platzierung_2 = st.number_input(f"Platzierung 2 ({player_name})", min_value=1, max_value=12, step=1)
                platzierung_3 = st.number_input(f"Platzierung 3 ({player_name})", min_value=1, max_value=12, step=1)
                platzierung_4 = st.number_input(f"Platzierung 4 ({player_name})", min_value=1, max_value=12, step=1)

                # Fehlstart Abfrage
                fehlstarts = st.number_input(f"Fehlstarts({player_name})", min_value=0)

                platzierung_set = [platzierung_1, platzierung_2, platzierung_3, platzierung_4]
                platzierungen_liste.append(platzierung_set)

                # Gesamtscore für den aktuellen Spieler berechnen
                gesamt_score = sum(platzierungen_mapping.get(p, 0) for p in platzierung_set)
                gesamt_scores_liste.append(gesamt_score)

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
