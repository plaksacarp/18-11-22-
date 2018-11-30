import pytest

from app.deposit import calculate_deposite

@pytest.mark.parametrize('deposit_amount, period_of_deposit, interest_rate, expected', [
    (100_000, 2, 0.07, 114000),
    (95_000, 3, 0.065, 113525),
    (151_000, 5, 0.085, 215175)
])
def test_deposit(deposit_amount, period_of_deposit, interest_rate, expected):
    actual = calculate_deposite(deposit_amount, period_of_deposit, interest_rate)
    assert expected == actual
