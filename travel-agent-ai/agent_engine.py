import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
# Importazioni dirette per evitare ImportError nel 2026
from langchain.agents.agent import AgentExecutor
from langchain.agents.tool_calling_agent.base import create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import travel_tools

load_dotenv()

def get_travel_agent():
    # Usiamo gemini-1.5-flash: veloce e gratuito
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    
    # SYSTEM PROMPT (Principi Capitolo 6: Agentic Pattern)
    # Istruiamo l'agente a pianificare e usare il web per evitare dati obsoleti
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Sei un AI Travel Engineer esperto. Il tuo compito è pianificare viaggi basandoti su dati REALI.
        
        LOGICA DI RAGIONAMENTO:
        1. RICERCA WEB: Se non conosci i prezzi attuali per il 2026 di voli o hotel, usa SEMPRE 'web_search'.
        2. ANALISI: Estrai dai risultati della ricerca le informazioni più economiche e rilevanti.
        3. BUDGET: Usa 'calculator' per verificare che la somma totale (Volo + Hotel + Pasti) sia inferiore al BUDGET.
        4. RISPOSTA: Presenta un itinerario strutturato giorno per giorno e una tabella dei costi."""),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # Creazione dell'agente moderno
    agent = create_tool_calling_agent(llm, travel_tools, prompt)
    
    # L'Executor gestisce il ciclo Thought -> Action -> Observation
    return AgentExecutor(agent=agent, tools=travel_tools, verbose=True, handle_parsing_errors=True)
