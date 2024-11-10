import os

from abc import ABC
import random
from model.city import City
from model.agent import Agent
from model.location import Location
current_dir = os.path.dirname(__file__)
move_up_dir = os.path.dirname(current_dir)


class SurvivorBot(Agent):
    def __init__(self, location: Location) -> None:
        super().__init__(location)
        # Inventory System. Only one slot available
        self.__inventory = []


    def act(self, city: City) -> None:
        self.__move(city)

    def __move(self, city: City) -> None:
        current_location = self.get_location()
        next_position_list = city.find_free_spot(current_location)
        next_position = random.choice(next_position_list)

        city.set_agent("SurviviorBot", next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

    def __pick_up(self):
        pass



