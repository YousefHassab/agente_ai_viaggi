from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

# Strumento per la ricerca web in tempo reale
web_search = DuckDuckGoSearchRun()

@tool
def calculator(expression: str) -> str:
    """Esegue calcoli matematici per il budget. Esempio: '150 * 3'"""
    try:
        # Nota: eval è usato qui per semplicità didattica
        return str(eval(expression))
    except Exception as e:
        return f"Errore nel calcolo: {e}"

travel_tools = [web_search, calculator]
