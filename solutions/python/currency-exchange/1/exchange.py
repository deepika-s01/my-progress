"""Functions for calculating steps in exchanging currency."""


def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    
    # Add spread to exchange rate
    rate_with_spread = exchange_rate * (1 + spread / 100)
    
    # Convert budget to foreign currency
    foreign_money = budget / rate_with_spread
    
    # Return only full bills
    return int(foreign_money // denomination) * denomination