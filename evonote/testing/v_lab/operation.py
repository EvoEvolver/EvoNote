from evonote.testing.v_lab.beaker import Beaker

"""
# Operations
In this module, we implement functions that can be used to operate the virtual lab.
"""

"""
## Salt water making
Here is a function that can be used to get a beaker of salt water.
"""


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


"""
## Sugar water making
Here is a function that can be used to get a beaker of sugar water.
"""


def get_a_beaker_of_sugar_water(water_volume: float, salt_weight: float) -> Beaker:
    """
    Get a beaker of sugar water.
    :param water_volume: The volume of water in the beaker. Should be less than 100.
    :param salt_weight: The weight of sugar in the beaker.
    :return: A beaker of salt water.
    """
    beaker = Beaker(100)
    beaker.add_liquid("water", water_volume)
    beaker.add_solid("sugar", salt_weight)
    """
    This ends the function
    """
    return beaker
