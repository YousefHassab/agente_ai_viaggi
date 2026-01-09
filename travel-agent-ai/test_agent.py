from tools import calculator
from agent_engine import get_travel_agent

def test_logic():
    assert calculator.invoke("10+10") == "20"
    assert get_travel_agent() is not None
