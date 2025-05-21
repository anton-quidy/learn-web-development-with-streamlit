import streamlit as st
from links import FROH, TRAURIG
import streamlit.components.v1 as components
import time
state = st.session_state
state["optionen"] = state.get("optionen", False)
state["Musik an"] = state.get("Musik an", False)
st.write(state["optionen"])

# Emojis: 😎 💻 🚀 😢 😁
# mehr Emojis gibt es hier: https://apps.timwhitlock.info/emoji/tables/unicode
start = st.button('Start')
if start:
    state["optionen"] = False
optionen = st.button('Optionen')
if optionen:
    state["optionen"] = True
if state["optionen"]:
    musik_option = st.selectbox ("Hintergrundmusik", ["an", "aus" , "wirklich aus"]) 
if "wirlich aus"  == "wirlich aus":
   state["Wirlich aus"] = True

beenden = st.button('Beenden')
if start:
    st.write("Du hast Start gewählt")
    st.write("Das Spiel beginnt...")
    state["optionen"] = False
if state["optionen"]:
    state ["optionen"] = True
    if musik_option == "an":
        audio_file = './Files/morning-garden-acoustic-chill-15013.mp3'
        st.audio(audio_file, format='audio/mpeg', start_time=0, autoplay=True, loop=True)
        zuruk = st.button("Zurück")
        if zuruk:
            state["optionen"] = False
            state["Musik an"] = True

            

    if musik_option == "aus":
        audio_file = './Files/male-what-6177(1).mp3'
        st.audio(audio_file , format='audio/mpeg', start_time=0, autoplay=True, loop=True)
    if musik_option == "wirklich aus":
        audio = './Files/huh-88084.mp3'
        st.audio(audio , format='audio/mpeg', start_time=0, autoplay=True, loop=True)
        if st.button("Audio wirklich sicher"):
            state ["optionen"] = False
            st.write("Bist du dir wirklich, wirklich , wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich sicher?")
            st.button("ja")
if beenden:
    st.write("Du hast Beenden gewählt")
    st.title("Du msst das jetzt spielen")
#if state["Musik an"]