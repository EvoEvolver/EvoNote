from evonote.testing.v_lab.beaker import Beaker


def get_a_beaker_of_salt_water(volume: float) -> Beaker:
    """
    Get a beaker of salt water.

    :param volume: The volume of the beaker.
    :return: A beaker of salt water.
    """
    beaker = Beaker(volume)
    beaker.add_liquid("salt water", volume)
    return beaker