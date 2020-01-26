from location import Location

class Parking(Location):
    def __init__(self, photo, id = 0, vacant = True):
        self.id = id
        self.vacant = vacant
        self.pic = photo

    def set_vacant(self, vacant):
        self.vacant = vacant

    def get_photo(self):
        return self.pic

    