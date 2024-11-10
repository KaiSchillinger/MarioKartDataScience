import streamlit as st
from authlib.integrations.requests_client import OAuth2Session

# Okta-Daten konfigurieren
client_id = st.secrets["OKTA_CLIENT_ID"]
client_secret = st.secrets["OKTA_CLIENT_SECRET"]
okta_domain = st.secrets["OKTA_DOMAIN"]

# OAuth2-Session starten
oauth = OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)
authorization_url, state = oauth.create_authorization_url(authorization_base_url)

# Authentifizierungs-Button in Streamlit
if "token" not in st.session_state:
    st.write("Bitte anmelden")
    if st.button("Mit Okta anmelden"):
        st.experimental_set_query_params(auth_url=authorization_url)

# Token nach der Authentifizierung abrufen
elif "code" in st.experimental_get_query_params():
    code = st.experimental_get_query_params()["code"]
    token = oauth.fetch_token(token_url, code=code)
    st.session_state["token"] = token
    st.write("Anmeldung erfolgreich!")
