import pytest
import sys
import os

# Add src to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.kpi_city import city_kpi

def test_city_kpi_happy_path():
    # Test with a valid city
    result = city_kpi("Mumbai")
    assert result is not None
    count, avg = result
    assert count > 0
    assert avg > 0

def test_city_kpi_injection_attempt():
    # Test with a malicious string
    # If injection worked, this would return ALL rows (count > 0).
    # Since we are secure, it searches for a city literally named "Mumbai' OR 1=1 --", finding nothing.
    result = city_kpi("Mumbai' OR 1=1 --")
    count, avg = result
    assert count == 0