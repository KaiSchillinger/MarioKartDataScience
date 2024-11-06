import streamlit as st

# Beispielhafte Streckenauswahl-Liste
streckenauswahl = ["Strecke A", "Strecke B", "Strecke C", "Strecke D"]

# Beispielhaftes platzierungen_mapping für die Score-Berechnung
platzierungen_mapping = {1: 10, 2: 8, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

# Anzahl der dynamischen Platzierungsspalten, hier als Beispiel
st.session_state.player_count = 3  # Beispielwert; kann dynamisch gesetzt werden

# Alle Spalten in einer Zeile erzeugen
cols = st.columns(1 + st.session_state.player_count)

# Streckenauswahl in der ersten Spalte
with cols[0]:
    st.subheader("Strecken")
    strecken_options = streckenauswahl
    strecke_1 = st.selectbox("Strecke 1", strecken_options)
    strecke_2 = st.selectbox("Strecke 2", strecken_options, index=1)
    strecke_3 = st.selectbox("Strecke 3", strecken_options, index=2)
    strecke_4 = st.selectbox("Strecke 4", strecken_options, index=3)
    strecken = [strecke_1, strecke_2, strecke_3, strecke_4]

# Dynamische Platzierungsspalten und Berechnung der Scores
platzierungen_liste = []  # Liste zum Speichern aller Platzierungen
gesamt_scores_liste = []  # Liste zum Speichern der Scores für jedes Platzierung-Set

for idx in range(st.session_state.player_count):
    with cols[idx + 1]:
        st.subheader(f"Platzierungen Set {idx + 1}")
        platzierung_1 = st.number_input(f"Platzierung 1 (Set {idx + 1})", min_value=1, max_value=12, step=1)
        platzierung_2 = st.number_input(f"Platzierung 2 (Set {idx + 1})", min_value=1, max_value=12, step=1)
        platzierung_3 = st.number_input(f"Platzierung 3 (Set {idx + 1})", min_value=1, max_value=12, step=1)
        platzierung_4 = st.number_input(f"Platzierung 4 (Set {idx + 1})", min_value=1, max_value=12, step=1)

        platzierung_set = [platzierung_1, platzierung_2, platzierung_3, platzierung_4]
        platzierungen_liste.append(platzierung_set)

        # Gesamtscore für das aktuelle Platzierung-Set berechnen
        gesamt_score = sum(platzierungen_mapping.get(p, 0) for p in platzierung_set)
        gesamt_scores_liste.append(gesamt_score)

# Anzeige der Gesamtscores für jedes Platzierung-Set
st.write("Gesamtpunkte für jedes Platzierung-Set:", gesamt_scores_liste)
