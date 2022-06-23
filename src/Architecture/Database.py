import Location


# Test change for github setup
class Database:
    """
    A class representing a database.
    The highest level organizational item so far...


    """
    locations = []
    # Temporary variables upgrade when implementing custom space development
    num_locations: int
    max_locations: int

    def add_location(self, location: Location) -> bool:
        if self.num_items >= self.max_items:
            return False
        else:
            self.locations.append(location)
            return True
