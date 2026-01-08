import streamlit as st
from agent_engine import get_travel_agent
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")
st.title("✈️ AI Travel Engineer")
st.markdown("Basato sui principi del **Capitolo 6 (Agenti)**")

with st.sidebar:
    st.header("Configurazione")
    budget = st.number_input("Budget Totale (€)", min_value=100, value=1000)
    days = st.slider("Durata (giorni)", 1, 14, 3)

destination = st.text_input("Dove vorresti andare?", placeholder="es: Tokyo, Parigi, Roma...")

if st.button("Pianifica Viaggio"):
    if destination:
        with st.spinner("L'agente sta consultando il web e calcolando il budget..."):
            try:
                agent = get_travel_agent()
                query = f"Pianifica un viaggio di {days} giorni a {destination} con un budget di {budget} euro."
                response = agent.invoke({"input": query})
                st.subheader("🗺️ Itinerario Suggerito")
                st.markdown(response["output"])
            except Exception as e:
                st.error(f"Errore: {e}")
    else:
        st.warning("Inserisci una destinazione!")
