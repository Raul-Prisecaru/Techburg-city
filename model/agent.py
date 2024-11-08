from location import Location
from abc import ABC, abstractmethod

class Agent:
    def __init__(self, location: Location) -> None:
        self.__location = location

    def get_location(self) -> Location:
        return self.__location
    
    def set_location(self, new_location: Location) -> None:
        self.__location = new_location

    @abstractmethod
    def act(self):
        pass