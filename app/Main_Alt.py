import streamlit as st
from links import FROH, TRAURIG
import streamlit.components.v1 as components
import time
#Main
state = st.session_state
state["optionen"] = state.get("optionen", False)
state["Musik an"] = state.get("Musik an", False)
st.write(state["optionen"])Start = st.container(border=False)


Beenden_container = st.container(border=True)
start = Start.button('Start')
if start:
    state["optionen"] = False

    if zuruk:
        state["optionen"] = False
        state["Musik an"] = True
        #st.write("Du hast Zurück gewählt")
        #state["optionen"] = False
#START
if start:
    Start.write("Du hast Start gewählt")
    Start.write("Das Spiel beginnt...")
    state["optionen"] = False
#OPTIONEN
Optionen_container = st.container(border=True)
optionen = Optionen_container.button('Optionen')
if optionen:
    state["optionen"] = True
if state["optionen"]:
    musik_option = Optionen_container.selectbox ("Hintergrundmusik", ["an", "aus" , "wirklich aus"]) 
if "wirlich aus"  == "wirlich aus":
   state["Wirlich aus"] = True
audio_file = './Files/morning-garden-acoustic-chill-15013.mp3'
if state["Musik an"]:
    audio_file = './Files/morning-garden-acoustic-chill-15013.mp3'
    st.audio(audio_file, format='audio/mpeg', start_time=0, autoplay=True, loop=True)
    zuruk = Optionen_container.button("Zurück")
if state["optionen"]:
    state ["optionen"] = True
    if musik_option == "an":
        state["Musik an"] = True
        
if musik_option == "aus":
        
    if musik_option == "wirklich aus":
        audio = './Files/huh-88084.mp3'
        Optionen_container.audio(audio , format='audio/mpeg', start_time=0, autoplay=True, loop=True)
        if Optionen_container.button("Audio wirklich sicher"):
            state ["optionen"] = False
            Optionen_container.write("Bist du dir wirklich, wirklich , wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich, wirklich sicher?")
            Optionen_container.button("ja")
#BEENDEN
beenden = Beenden_container.button('Beenden')
if beenden:
    st.write("Du hast Beenden gewählt")
    st.title("Du msst das jetzt spielen")
