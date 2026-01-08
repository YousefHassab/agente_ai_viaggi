import streamlit as st
from agent_engine import get_travel_agent
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Engineer")
st.markdown("Basato sui principi del **Capitolo 6 (Agenti)**")

# Pannello laterale per i parametri del viaggio
with st.sidebar:
    st.header("Parametri Viaggio")
    budget = st.number_input("Budget Totale (€)", min_value=100, value=1000)
    days = st.slider("Durata del viaggio (giorni)", 1, 15, 3)

# Campo di testo principale
destination = st.text_input("Dove vorresti andare o che tipo di viaggio cerchi?", 
                             placeholder="es: Un weekend romantico a Parigi o 5 giorni a Tokyo")

if st.button("Pianifica il mio Viaggio"):
    if destination:
        with st.spinner("L'agente sta pianificando, cercando i costi e calcolando il budget..."):
            try:
                agent = get_travel_agent()
                # Creiamo la query per l'agente
                prompt = f"Pianifica un viaggio di {days} giorni a {destination}. Il budget totale è di {budget} euro. Includi stime dei costi reali trovate sul web."
                
                # Eseguiamo l'agente
                response = agent.invoke({"input": prompt})
                
                st.subheader("🗺️ Itinerario Suggerito")
                st.write(response["output"])
            except Exception as e:
                st.error(f"Si è verificato un errore durante la pianificazione: {e}")
    else:
        st.warning("Inserisci una destinazione per iniziare!")
