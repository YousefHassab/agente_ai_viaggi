from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

# Strumento per la ricerca web (RAG Dinamico)
web_search = DuckDuckGoSearchRun()

@tool
def calculator(expression: str) -> str:
    """Esegue calcoli matematici per il budget. Esempio: '150 + 400'"""
    try:
        # Nota: usiamo eval per semplicità didattica
        return str(eval(expression))
    except:
        return "Errore nel calcolo."

travel_tools = [web_search, calculator]
