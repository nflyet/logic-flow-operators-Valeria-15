import pytest
from ticket_pricing import calculate_ticket_price

def test_child_ticket_weekday():
    assert calculate_ticket_price(8, False, False) == 20  # Assuming $20 for a child on a weekday

def test_adult_ticket_weekend():
    assert calculate_ticket_price(25, True, False) == 40  # Assuming $40 for an adult on a weekend

def test_senior_ticket_holiday():
    assert calculate_ticket_price(65, False, True) == 30  # Assuming $30 for a senior on a holiday

# Add more test cases to cover different scenarios