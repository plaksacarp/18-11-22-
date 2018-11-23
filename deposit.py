def calculate_deposite(deposit_amount, period_of_deposit, interest_rate):
    # сумма вклада, срок вклада, процентная ставка
    """
    >>> calculate_deposite(100_000, 2, 0.07)
    114000.0

    >>> calculate_deposite(95_000, 3, 0.065)
    113525.0
    """
    accrued_interest = deposit_amount * interest_rate * period_of_deposit
    total_deposite = deposit_amount + accrued_interest
    return total_deposite


print(calculate_deposite(50_000, 1, 0.08))
