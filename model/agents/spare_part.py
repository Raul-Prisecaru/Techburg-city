from __future__ import annotations
from random import random, randint
from typing import TYPE_CHECKING, List, Literal
from model.location import Location
if TYPE_CHECKING:
    from model.city import City



class SparePart:

    def __init__(self, city: City, size: Literal["small", "medium", "large"], enhancement: Literal["speed", "vision", "energy"]):
        self.__city: City = city
        self.__location: Location = None
        self.__size: Literal["small", "medium", "large"] = size
        self.__enhancement: Literal["speed", "vision", "energy"] = enhancement

    def get_location(self):
        return self.__location


    def get_size(self):
        return self.__size


    def set_size(self, newSize: Literal["small", "medium", "large"]):
        self.__size = newSize

    def get_enhancement(self):
        return self.__enhancement

    def set_enhancement(self, newEnhancement: Literal["speed", "vision", "energy"]):
        self.__enhancement = newEnhancement


    def add_specific_spot(self, location: Location):
        self.__location = location
        self.__city.add_object(location, self)


    def randomly_scatter(self, start_location: int, end_location: int) -> None:
        """
        Function responsible for randomly scattering Spare Part's Around the environment
            Parameter:
                number_spareParts (int): Total Number of Spare Parts to be scattered around
                startLocation (int): Minimum width to add Spare Parts to
                endLocation (int): Maximum width to add Spare Parts to

            Return:
                None
        """

        while True:
            location = Location(randint(start_location, end_location), randint(start_location, end_location))

            if self.__city.check_space_if_None(location):
                self.__city.add_object(location, self)
                break

            else:
                continue






