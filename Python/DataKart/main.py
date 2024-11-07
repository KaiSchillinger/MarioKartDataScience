import streamlit as st
import home
import KartStat
import auswertung

# Sidebar für die Seitenauswahl
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Wähle eine Seite", ["Home", "Neue Einträge", "Daten"])

# Seiten basierend auf der Auswahl aufrufen
if page == "Home":
    home.show()
elif page == "Neue Einträge":
    KartStat.show()
elif page == "Daten":
    auswertung.show()
