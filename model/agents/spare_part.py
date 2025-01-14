from __future__ import annotations
from random import random, randint
from typing import TYPE_CHECKING, List, Literal

if TYPE_CHECKING:
    from model.city import City
    from model.location import Location


class SparePart:

    def __init__(self, city: City):
        self.__city: City = city
        self.__location: Location = None
        self.__size: Literal["Small", "Medium", "Large"] = None
        self.__enhancement: Literal["Speed", "Vision", "Energy"] = None

    def get_location(self):
        return self.__location


    def get_size(self):
        return self.__size


    def set_size(self, newSize: Literal["Small", "Medium", "Large"]):
        self.__size = newSize

    def get_enhancement(self):
        return self.__enhancement

    def set_enhancement(self, newEnhancement: Literal["Speed", "Vision", "Energy"]):
        self.__enhancement = newEnhancement


    def add_specific_spot(self, location: Location):
        self.__location = location
        self.__city.add_object(location, self)


    def randomly_scatter(self, number_spare_parts: int, start_location: int, end_location: int) -> None:
        """
        Function responsible for randomly scattering Spare Part's Around the environment
            Parameter:
                number_spareParts (int): Total Number of Spare Parts to be scattered around
                startLocation (int): Minimum width to add Spare Parts to
                endLocation (int): Maximum width to add Spare Parts to

            Return:
                None
        """

        spare_parts_locations: List[Location] = []

        while len(spare_parts_locations) != number_spare_parts:
            location = Location(randint(start_location, end_location), randint(start_location, end_location))

            if self.__city.check_space_if_None(location):

                for spare_location in spare_parts_locations:

                    if location == spare_location:
                        continue

                spare_parts_locations.append(location)

            else:
                continue

        self.__city.add_objects_to_map(spare_parts_locations, self)






