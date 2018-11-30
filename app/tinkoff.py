def calculate_cashback_to_card(ordinary_amount, cashback_amount, special_offer_amount):
    """
    >>> calculate_cashback_to_card(1000, 700, 500)
    195.0

    >>> calculate_cashback_to_card(4000, 1000, 100)
    120.0
    """
    ordinary_percent = 0.01
    cashback_percent = 0.05
    special_offer_percent = 0.3

    cashback_ordinary_amount = ordinary_amount * ordinary_percent
    cashback_high_cashback_amount = cashback_amount * cashback_percent
    cashback_special_offer_amount = special_offer_amount * special_offer_percent
    total_cashback = cashback_ordinary_amount + cashback_high_cashback_amount + cashback_special_offer_amount

    return total_cashback


print(calculate_cashback_to_card(8000, 5000, 300))
