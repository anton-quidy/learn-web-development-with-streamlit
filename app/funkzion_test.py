


import streamlit as st
import time

def starte_spiel(state):
    links, mitte , rechts = st.columns(3)

# Initialisierung von States
    if "gestartet" not in st.session_state:
        st.session_state.gestartet = False
    if "Spiel" not in st.session_state:
        st.session_state.Spiel = False

# Button nur anzeigen, wenn Spiel nicht gestartet wurde
    if not st.session_state.gestartet:
        with mitte:
            if st.button("Start"):
                st.session_state.Spiel = True

# Ladebildschirm abarbeiten, wenn Spiel-Start gedrückt wurde
    if st.session_state.Spiel and not st.session_state.gestartet:
        with st.spinner("Wait for it..."):
            st.toast("Loading...")
            time.sleep(1)
            st.toast("Loading Grafic...")
            time.sleep(1)
            st.toast("Loading Sound...")
            time.sleep(1)
            st.toast("Loading Game...")
            time.sleep(1)
            st.toast("Loading Mods...")
            for percent in range(10, 100, 10):
                time.sleep(0.1)
                st.toast(f"{percent}%")
            st.toast("102%")  
            time.sleep(1)
            st.toast("Done!")

        st.session_state.gestartet = True               


#def spielablauf(state):
    if ""