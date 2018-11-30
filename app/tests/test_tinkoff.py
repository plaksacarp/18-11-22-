import pytest

from app.tinkoff import calculate_cashback_to_card

@pytest.mark.parametrize('ordinary_amount, cashback_amount, special_offer_amount, expected', [
    (1000, 700, 500, 195),
    (4000, 1000, 100, 120),
    (8000, 5000, 300, 420)
])
def test_tinkoff(ordinary_amount, cashback_amount, special_offer_amount, expected):
    actual = calculate_cashback_to_card(ordinary_amount, cashback_amount, special_offer_amount)
    assert expected == actual
