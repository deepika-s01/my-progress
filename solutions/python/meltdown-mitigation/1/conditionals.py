"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    A reactor is balanced if:
    - temperature < 800
    - neutrons_emitted > 500
    - temperature * neutrons_emitted < 500000
    """
    
    if temperature < 800:
        if neutrons_emitted > 500:
            if temperature * neutrons_emitted < 500000:
                return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
    
    Efficiency = (generated_power / theoretical_max_power) * 100
    where generated_power = voltage * current
    """
    
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.
    
    - LOW -> value < 90% of threshold
    - NORMAL -> within ±10% of threshold
    - DANGER -> outside above ranges
    """
    
    value = temperature * neutrons_produced_per_second
    lower_limit = 0.9 * threshold
    upper_limit = 1.1 * threshold

    if value < lower_limit:
        return "LOW"
    elif lower_limit <= value <= upper_limit:
        return "NORMAL"
    else:
        return "DANGER"