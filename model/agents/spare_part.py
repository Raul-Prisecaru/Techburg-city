from random import random, randint

from model.agent import Agent
from model.location import Location
from model.city import City

class SparePart(Agent):

    def __init__(self, location: Location):
        super().__init__(location)

    # For Set Location:: IDEA
    #     Check if the position matches with one of the
    #     Recharge Stations and display that
    # E.g Location: Recharge Station 1 // coords: (x : y)


    def act(self, city: City):
        self.__randomly_scatter(city)

    # Scatter between coordinates 10 - 20
    # Later to dynamically adapt
    # Get width and height and subtract 10 from each
    def __randomly_scatter(self, city: City):
        spare_parts_locations = []
        while len(spare_parts_locations) != 10:
            location = Location(randint(10, 20), randint(10, 20))

            if city.check_space(location):
                spare_parts_locations.append(location)
            else:
                continue



