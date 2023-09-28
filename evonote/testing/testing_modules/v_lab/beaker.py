from doc_in_py.decorator import example


class Beaker:
    """
    A beaker is a container that can hold a certain volume of liquid.
    This class is used to represent the beaker in the virtual lab.
    """

    def __init__(self, max_volume: float):
        """
        Create a beaker with a maximum volume.
        :param max_volume: The maximum volume of the beaker.
        """
        self.max_volume = max_volume
        self.contents = []

    """
    ## Operations of beaker
    """

    def add_liquid(self, liquid_type: str, volume: float) -> bool:
        """
        :param liquid_type: The type of liquid, e.g. water, ethanol, etc.
        :param volume: The volume of the liquid added.
        :return: whether the liquid was successfully added.
        """
        if self.current_volume() + volume > self.max_volume:
            return False
        self.contents.append((liquid_type, volume))
        return True

    def add_solid(self, solid_type: str, weight: float) -> bool:
        """
        :param solid_type: The type of solid, e.g. salt, sugar, etc.
        :param weight: The weight of the solid added.
        :return: whether the solid was successfully added.
        """
        self.contents.append((solid_type, weight))
        return True

    """
    ## Status of beaker
    """

    def current_volume(self) -> float:
        """
        :return: The current volume of the beaker.
        """
        return sum([c[1] for c in self.contents])

class Desk:
    """
    A desk is for holding beakers. It can hold multiple beakers.
    """
    def __init__(self):
        self.beakers = []

@example
def put_beaker_on_desk():
    """
    Here is an example of putting a beaker on a desk.
    """
    desk = Desk()
    beaker = Beaker(100)
    desk.beakers.append(beaker)
    return desk