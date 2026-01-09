import streamlit as st
from agent_engine import get_travel_agent
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Engineer")
st.markdown("Applicazione basata sui principi del **Capitolo 6 (Agenti)**")

# Configurazione tramite Sidebar
with st.sidebar:
    st.header("Parametri del Viaggio")
    budget = st.number_input("Budget Totale (€)", min_value=100, value=1000)
    days = st.slider("Durata (giorni)", 1, 14, 3)
    st.info("L'agente cercherà dati reali su voli e hotel per il 2026.")

destination = st.text_input("Dove vuoi andare?", placeholder="es: Tokyo, Parigi, un weekend a Roma...")

if st.button("Pianifica Viaggio"):
    if destination:
        with st.spinner("L'agente sta consultando il web e calcolando i costi..."):
            try:
                # 1. Inizializza l'Agente
                agent = get_travel_agent()
                
                # 2. Crea la query (Integrazione della Ricerca Web)
                # L'agente userà questa query per decidere quali strumenti attivare
                query = f"Pianifica un viaggio di {days} giorni a {destination} con un budget di {budget} euro. Usa la ricerca web per trovare prezzi reali aggiornati al 2026."
                
                # 3. Esecuzione
                response = agent.invoke({"input": query})
                
                st.subheader("🗺️ Itinerario e Budget")
                st.markdown(response["output"])
                
            except Exception as e:
                st.error(f"Errore durante la pianificazione: {e}")
    else:
        st.warning("Inserisci una destinazione!")
