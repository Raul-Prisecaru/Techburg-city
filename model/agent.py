from location import Location

class Agent:
    def __init__(self, location: Location):
        self.__location = location

    def get_location(self):
        return self.__location
    
    def set_location(self, new_location: Location):
        self.__location = new_location