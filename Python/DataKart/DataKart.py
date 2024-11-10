import streamlit as st
import pandas as pd
import os


# Dateiname für den Datensatz
datafile = '../CSV_DATA/data.csv'


# Funktion, um den Datensatz zu laden oder zu erstellen
@st.cache_data
def load_data():
    if os.path.exists(datafile):
        return pd.read_csv(datafile)
    else:
        # Leerer DataFrame mit den angegebenen Spalten
        return pd.DataFrame(columns=["id", "spieler", "platzierung", "controller", "strecken",
                                     "drink_count", "kiff_count", "datum", "rennen_tag",
                                     "gesamt_score", "beamer", "fehlstarts"])


# Funktion, um den Datensatz zu speichern
def save_data(data):
    data.to_csv(datafile, index=False)


# DF Strecken
try:
    df_strecken = pd.read_csv('../../Zusatzdaten/strecken_cups.csv').sort_values('Strecke')
    streckenauswahl = df_strecken['Strecke'].tolist()
except FileNotFoundError:
    st.error("Die Datei 'strecken_cups.csv' wurde nicht gefunden.")
    streckenauswahl = []

# DF Scores
try:
    df_scores = pd.read_csv('../../Zusatzdaten/scores.csv')
    platzierungen_mapping = df_scores.set_index('platz')['punkte'].to_dict()
except FileNotFoundError:
    st.error("Die Datei 'scores.csv' wurde nicht gefunden.")
    platzierungen_mapping = {}

# Controller
controller_options = ["Pro", "Minus Blau", "Plus Rot", "Minus Gelb", "Plus Gelb"]

# Spielernamen auswahl
namen_auswahl = ['Daniel', 'Kai', 'Niclas', 'Amine', 'Christof', 'David', 'Joe', 'Lina', 'Patrick', 'PKai', 'Robin']

st.title('MarioKart')
st.write('Willkommen')