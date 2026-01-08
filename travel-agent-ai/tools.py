from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

# Strumento per cercare informazioni aggiornate (voli, hotel, meteo)
web_search = DuckDuckGoSearchRun()

@tool
def calculator(expression: str) -> str:
    """Esegue calcoli matematici per il budget (es. somme o moltiplicazioni)."""
    try:
        # Nota: eval è usato qui per semplicità didattica
        return str(eval(expression))
    except Exception as e:
        return f"Errore: {e}"

# Lista degli strumenti per l'agente
travel_tools = [web_search, calculator]
