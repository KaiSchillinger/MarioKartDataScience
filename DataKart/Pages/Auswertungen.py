import streamlit as st
import matplotlib.pyplot as plt
import ast
from DataKart import load_data, farben

st.header('Auswertungen')

# Daten laden
data_analyse = load_data()

tabs = st.tabs(['GesamtScore'])

with tabs[0]:
    st.subheader("Durchschnittlicher Gesamt-Score pro Spieler")

    # Konvertiere die Spalte 'platzierung' in Listen von Integern
    data_analyse['platzierung'] = data_analyse['platzierung'].apply(ast.literal_eval)

    # Berechne die durchschnittliche Platzierung pro Spieler
    data_analyse['avg_platzierung'] = data_analyse['platzierung'].apply(lambda x: sum(x) / len(x))
    df_avg_score = data_analyse.groupby('spieler')['gesamt_score'].mean().reset_index(name='avg_gesamt_score')

    # Sortiere die Daten absteigend nach 'avg_gesamt_score'
    df_avg_score_sorted = df_avg_score.sort_values(by='avg_gesamt_score', ascending=False)

    # Darstellung der durchschnittlichen Platzierung mit horizontalen Balken in absteigender Reihenfolge
    fig, ax = plt.subplots(figsize=(8, 2))
    df_avg_score_sorted.plot(kind='barh', x='spieler', y='avg_gesamt_score', ax=ax, width=0.5, color=farben(len(df_avg_score_sorted)))
    ax.invert_yaxis()  # Y-Achse umkehren, damit der höchste Wert oben ist
    ax.get_legend().set_visible(False)

    # Werte in den Balken anzeigen
    for index, value in enumerate(df_avg_score_sorted['avg_gesamt_score']):
        ax.text(value * 0.05, index, f'{value:.2f}', va='center')  # va='center' sorgt für mittige Ausrichtung

    st.pyplot(fig)
