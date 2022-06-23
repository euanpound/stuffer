import Item


class Location:
    """
    A class representing an individual storage location
    """
    item: [Item]
    storage_capacity: int
    size: Item.Size

    def __init__(self, storage_capacity, size: Item.Size):
        self.storage_capacity = storage_capacity
        self.size = size

    def __init__(self, storage_capacity, x: int, y: int, z: int):
        self.storage_capacity = storage_capacity
        self.size.x = x
        self.size.y = y
        self.size.z = z

    def get_remaining_storage(self) -> Item.Size:
        # Calculate the remaining size in the current location
        remaining_size: Item.Size
        remaining_size.x = self.size.x
        remaining_size.y = self.size.y
        remaining_size.z = self.size.z
        for item in self.item:
            remaining_size.x -= item.size.x
            remaining_size.y -= item.size.y
            remaining_size.z -= item.size.z
        return remaining_size

    def add_item(self, item: Item) -> bool:
        # Add item to the storage Location and return True if success
        if self.has_room(item):
            self.item = item
            return True
        return False

    def remove_item(self) -> bool:
        # Remove the item in storage return False if no item or True if success
        if self.item:
            item = None
            return True
        return False

