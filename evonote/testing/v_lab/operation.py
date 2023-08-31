from evonote.testing.v_lab.beaker import Beaker


def get_a_beaker_of_salt_water(water_volume: float, salt_weight: float) -> Beaker:
    """
    Get a beaker of salt water.
    :param water_volume: The volume of water in the beaker. Should be less than 100.
    :param salt_weight: The weight of salt in the beaker.
    :return: A beaker of salt water.
    """
    beaker = Beaker(100)
    beaker.add_liquid("water", water_volume)
    beaker.add_solid("salt", salt_weight)
    return beaker
