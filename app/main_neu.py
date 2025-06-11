import streamlit as st
import time

from functions import starte_spiel
#from functions import spielablauf

state = st.session_state

starte_spiel(state)
#spielablauf(state)

