import pytest
from tools import calculator
from agent_engine import get_travel_agent

def test_calculator_logic():
    # Verifica che la calcolatrice faccia 2+2
    result = calculator.invoke("2 + 2")
    assert result == "4"

def test_calculator_complex():
    # Verifica calcoli più complessi (es. budget giornaliero)
    result = calculator.invoke("1500 / 5")
    assert result == "300.0"

def test_agent_initialization():
    # Verifica che il "cervello" dell'agente si carichi correttamente
    agent = get_travel_agent()
    assert agent is not None
