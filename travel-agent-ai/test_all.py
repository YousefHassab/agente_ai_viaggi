import pytest
from tools import calculator
from agent_engine import get_travel_agent

def test_calculator():
    assert calculator.invoke("100 + 200") == "300"

def test_agent_creation():
    agent = get_travel_agent()
    assert agent is not None
