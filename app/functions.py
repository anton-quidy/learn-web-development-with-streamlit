import streamlit as st


def starte_spiel(state):

    Start = st.container(border=False)
    state["Spiel"] = state.get("Spiel", False)
    state["Spiel"] = False
    if state["Spiel"] == False:
        start = Start.button('Start')
        if start:
            #state["Spiel"] = True
            # Was passiert beim Spiel
 

    if state["Spiel"] == True:
        Start.write("Du hast Start gewählt")
        Start.write("Das Spiel beginnt...")
        