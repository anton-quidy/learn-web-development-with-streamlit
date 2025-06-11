import streamlit as st
import time
import random


def starte_spiel(state):
    state["gestartet"] = state.get("gestartet", False)
    state["o"] = state.get("o", False)   
    links , mitte , rechts = st.columns(3)
    
    state["Spiel"] = state.get("Spiel", False)
    
    zeige_start_button = state["Spiel"] == False and state["gestartet"] == False and state["o"] == False

    if zeige_start_button:
         with mitte:
            state["Spiel"] = mitte.button('Start')
        
    lade_bildschirm = state["Spiel"] and state["gestartet"] == False and state["o"] == False

    if lade_bildschirm:
        zeige_ladebildschirm()
        state["gestartet"] = True
        state["Spiel"] = False
     
     
    if state["gestartet"] == True and state["Spiel"] == False:
        
        rechts.button('3 Spieler')
        if links.button('4 Spieler'):
            state["gestartet"] = False
            state["o"] = True



    if state["gestartet"] == False and state["Spiel"] == False and state["o"] == True:
        meine_sätze = [
                "Hilde geht schopen",
                "Adrian muss in die Stadt",
                "Dorffest ohne Günter",
                "Günter bekommt kein Bier",
                "Opa geht in die Kneipe",
                "Lutz schrumpft",
                "Anton hat keine Zeit",
                "Adrian ohne die Mediatek"
            ]

            
        mein_satz = random.choice(meine_sätze)
        mitte.title (mein_satz)














       

    # Ablauf des Spiel
    # 1. Spieler 1 ist an der Reihe und wird angezigt
    # 2. Spieler 1 ziet karten bis er  fünf Karten hat 
    # 3. Spieler 1 kann eine Karte ablegen
    # 4. Kurze warte Zeit
    
     # 5. Spieler 2 ist an der Reihe und wird angezigt
    # 6. Spieler 2 ziet karten bis er  fünf Karten hat 
    # 7. Spieler 2 kann eine Karte ablegen
    # 8. Kurze warte Zeit

     # 9. Spieler 3 ist an der Reihe und wird angezigt
    # 10. Spieler 3 ziet karten bis er  fünf Karten hat 
    # 11. Spieler 3 kann eine Karte ablegen
    # 12. Kurze warte Zeit



    #spalten

    def zeige_ladebildschirm():
        with st.spinner("Wait for it...", show_time=False):
            msg = st.toast("Loading...")
            time.sleep(1)
            msg.toast("Loading Grafic...")
            time.sleep(1)
            msg.toast("Loading Sound...")
            time.sleep(1)
            msg.toast("Loading Game...")
            time.sleep(1)
            msg.toast("Loading Mods...")
            time.sleep(0.1)
            msg.toast("10%")
            time.sleep(0.1)
            msg.toast("20%")
            time.sleep(0.1)
            msg.toast("30%")
            time.sleep(0.1)
            msg.toast("40%")
            time.sleep(0.1)
            msg.toast("50%")
            time.sleep(0.1)
            msg.toast("60%")
            time.sleep(0.1)
            msg.toast("70%")
            time.sleep(0.1)
            msg.toast("80%")
            time.sleep(0.1)
            msg.toast("90%")
            time.sleep(0.1)
            msg.toast("102%")
            time.sleep(4)
            msg.toast("Done!")