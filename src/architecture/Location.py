import Item


class Location:
    """
    A class representing an individual storage location
    """
    item: [Item]
    storage_capacity: int
    size: Item.Size

    def __init__(self, storage_capacity):
        self.storage_capacity = storage_capacity

    def has_room(self, item: Item) -> bool:
        # Guarantee the Location in storage has room
        if item.size < self.storage_capacity:
            return True
        return False

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

