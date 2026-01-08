import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
# Importazione esplicita per evitare conflitti di versione
from langchain.agents.agent import AgentExecutor
from langchain.agents.tool_calling_agent.base import create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import travel_tools

load_dotenv()

def get_travel_agent():
    # Usiamo gemini-1.5-flash: ha i limiti di quota più generosi per gli agenti
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    
    # SYSTEM PROMPT (Principi Capitolo 6: Pianificazione e Strumenti)
    # Definiamo l'identità dell'agente e come deve integrare la ricerca web
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Sei un AI Travel Engineer esperto.
        Il tuo compito è pianificare viaggi basandoti su dati REALI.
        
        INTEGRAZIONE RICERCA WEB (Cap. 6):
        1. Se l'utente chiede prezzi di voli o hotel per il 2026, usa 'web_search'.
        2. Analizza i risultati per estrarre informazioni aggiornate.
        3. Usa 'calculator' per verificare che la somma non superi il BUDGET.
        
        REGOLE:
        - Rispondi in italiano.
        - Se il budget è troppo basso, proponi alternative economiche o riduci i giorni."""),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # Creazione dell'agente (Metodo moderno Tool Calling)
    agent = create_tool_calling_agent(llm, travel_tools, prompt)
    
    # L'Executor gestisce il ciclo Thought -> Action -> Observation
    return AgentExecutor(agent=agent, tools=travel_tools, verbose=True, handle_parsing_errors=True)
