def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active:
        if touching_ghost:
            return True
    return False
def score(touching_power_pellet, touching_dot):
    if touching_power_pellet:
        return True
    if touching_dot:
        return True
    return False
def lose(power_pellet_active, touching_ghost):
    if touching_ghost:
        if not power_pellet_active:
            return True
    return False
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots:
        if not lose(power_pellet_active, touching_ghost):
            return True
    return False