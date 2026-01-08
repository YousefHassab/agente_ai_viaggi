import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.agents import initialize_agent, AgentType
from tools import travel_tools

load_dotenv()

def get_travel_agent():
    # Usiamo Llama 3.3 su Groq: velocità istantanea e quota generosa
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.1)
    
    instructions = """Sei un AI Travel Engineer. 
    REGOLE AGENTICHE (Cap. 6):
    1. PIANIFICAZIONE: Usa 'web_search' per trovare i prezzi reali ad oggi.
    2. BUDGET: Assicurati che il totale sia inferiore al budget dell'utente.
    3. STRUMENTI: Usa 'calculator' per sommare i costi.
    4. RISPOSTA: Rispondi in italiano con itinerario e costi stimati."""

    agent = initialize_agent(
        tools=travel_tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        agent_kwargs={"prefix": instructions}
    )
    
    return agent
