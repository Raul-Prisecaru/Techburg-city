from __future__ import annotations
from random import random, randint
from typing import TYPE_CHECKING, List

from model.agent import Agent
from model.location import Location

if TYPE_CHECKING:
    from model.city import City

class SparePart:

    def __init__(self, city: City):
        self.__city = city


    def add_specific_spot(self, location: Location):
        self.__city.add_objects_to_map(location, self)

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






