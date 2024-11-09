from model.location import Location
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Imports City file if it being used for Type Checking
# Needed to avoid Circular Imports here
if TYPE_CHECKING:
    from city import City

class Agent:
    # Agent Class Takes a Location Class
    def __init__(self, location: Location) -> None:
        self.__location = location

    # Returns the Location set for the Agent
    def get_location(self) -> Location:
        return self.__location

    # Sets new Location
    def set_location(self, new_location: Location) -> None:
        self.__location = new_location

    # Abstract used to define what Act does for different Agent
    # Takes City Class to define which environment to execute different Acts on
    @abstractmethod
    def act(self, city: "City"):
        pass