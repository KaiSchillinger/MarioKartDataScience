import streamlit as st
import pandas as pd
import datetime
from DataKart import load_data, save_data, streckenauswahl, platzierungen_mapping, controller_options, namen_auswahl


# DataFrame neue Daten
new_data = pd.DataFrame(
    columns=["id", "spieler", "platzierung", "controller", "strecken", "drink_count", "kiff_count",
             "datum", "rennen_tag", "gesamt_score", "beamer", "fehlstarts"])

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

    st.session_state.player_data = []  # Liste zurücksetzen

    with col1:
        st.session_state.players = []

        for i in range(st.session_state.player_count):
            player_name = st.selectbox(f"Spieler {i + 1} Name", namen_auswahl, index=i)
            st.session_state.players.append(player_name)

    with (col2):
        st.session_state.drinks = []

        for i in range(st.session_state.player_count):
            drink_count = st.number_input(f"Drink Count SP {i +1}", min_value=0)
            st.session_state.drinks.append(drink_count)

    with col3:
        st.session_state.kiffs = []

        for i in range(st.session_state.player_count):
            kiff_count = st.number_input(f"Kiff Count SP {i +1}", min_value=0)
            st.session_state.kiffs.append(kiff_count)

    with col4:
        st.session_state.rennen_nr = []

        for i in range(st.session_state.player_count):
            rennen_tag = st.number_input(f"RennenNr. SP {i +1}", min_value=0)
            st.session_state.rennen_nr.append(rennen_tag)

    with col5:
        st.session_state.controller_list = []

        for i in range(st.session_state.player_count):
            controller = st.selectbox(f"Controller SP {i +1}", controller_options)
            st.session_state.controller_list.append(controller)

    if st.button("Weiter"):

        # Speichere Grunddaten für jeden Spieler
        for i in range(st.session_state.player_count):
            st.session_state.player_data.append({
                "id": next_id + i,
                "spieler": st.session_state.players[i],
                "drink_count": st.session_state.drinks[i],
                "kiff_count": st.session_state.kiffs[i],
                "rennen_tag": st.session_state.rennen_nr[i],
                "controller": st.session_state.controller_list[i],
                "datum": datum,
                "beamer": beamer,
            })

        st.session_state.step = 3  # Weiter zu Schritt 3

# Step 3: Dateneingabe für jeden Spieler
elif st.session_state.step == 3:

    # Spalten für Strecken und dynamische Spalten Platzierungen
    cols = st.columns(1 + st.session_state.player_count)

    # Streckenauswahl in der ersten Spalte
    with cols[0]:
        st.subheader("Strecke")
        strecken = [st.selectbox(f"Strecke {i + 1}", streckenauswahl, index=i) for i in range(4)]

    platzierungen_liste = []  # Liste zum Speichern aller Platzierungen
    gesamt_scores_liste = []  # Liste zum Speichern der Scores für jedes Platzierung-Set

    # Spalten für Platzierungen erstellen und Spielernamen als Überschriften setzen
    for idx, col in enumerate(cols[1:]):  # Ab cols[1] beginnen, da cols[0] für Strecken reserviert ist
        player_name = st.session_state.players[idx] if idx < len(st.session_state.players) else f"Spieler {idx + 1}"

        with col:
            st.subheader(player_name)
            platzierungen = [st.number_input(f"Platzierung {j + 1} ({player_name})",
                                             min_value=1, max_value=12, step=1) for j in range(4)]
            fehlstarts = st.number_input(f"Fehlstarts ({player_name})", min_value=0)

            # Gesamtscore berechnen und Platzierungen hinzufügen
            gesamt_score = sum(platzierungen_mapping.get(p, 0) for p in platzierungen)
            gesamt_scores_liste.append(gesamt_score)
            platzierungen_liste.append(platzierungen)

            # Spieler-Daten aktualisieren
            st.session_state.player_data[idx].update({
                "strecken": strecken,
                "platzierung": platzierungen,
                "gesamt_score": gesamt_score,
                "fehlstarts": fehlstarts
            })

    if st.button("Daten speichern!"):
        # Neue Daten zur Tabelle hinzufügen
        player_data_frames = []  # Liste, um alle Player-DataFrames zwischenzuspeichern

        for player_data in st.session_state.player_data:
            player_data_frames.append(pd.DataFrame([player_data]))  # Jeden Spieler als DataFrame hinzufügen

        # Alle DataFrames zu einem großen DataFrame zusammenfügen
        new_data = pd.concat([data] + player_data_frames, ignore_index=True)

        # Speichern und anzeigen
        save_data(new_data)
        st.write("Daten gespeichert!")
        st.write(new_data)

        # Schritt zurücksetzen
        st.session_state.step = 1
