import streamlit as st
import matplotlib.pyplot as plt
import ast
from DataKart import load_data

# Daten laden
data_analyse = load_data()

st.title("Analysen")

# Konvertiere die Spalte 'platzierung' in Listen von Integern
data_analyse['platzierung'] = data_analyse['platzierung'].apply(ast.literal_eval)

# Berechne die durchschnittliche Platzierung pro Spieler
data_analyse['avg_platzierung'] = data_analyse['platzierung'].apply(lambda x: sum(x) / len(x))
df_avg_score = data_analyse.groupby('spieler')['gesamt_score'].mean().reset_index(name='avg_gesamt_score')

# Darstellung der durchschnittlichen Platzierung
fig, ax = plt.subplots()
df_avg_score.plot(kind='bar', x='spieler', y='avg_gesamt_score', ax=ax)
st.pyplot(fig)
