import Location


class Item:
    """
    A class representing a single item stored in the database

        id is the unique identification number of the item
            could be a barcode

    """
    identification: int
    size: int

    def __init__(self, identification, size):
        self.identification = identification
        self.size = size


class Size:
    """
    A class representing the 3d size of an item
    """
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x & self.y == other.y & self.z == other.z
