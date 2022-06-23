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

    def get_id(self):
        return self.identification
