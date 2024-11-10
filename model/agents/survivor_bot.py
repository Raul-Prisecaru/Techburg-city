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


    # This will basically act like a priority List
    # In will do the most important thing first to last
    # e.g First check for enemies around, second check for spare part
    # Might be something like this in order:
    """
    Priority list (In order)
    - Check for enemies (drones / nanobots) around -> Run away to nearest recharge station
    - Check for spare part around -> Pick up and go to nearest recharge station
    """
    def act(self, city: City) -> None:

        self.__move_to_free_spot(city)

    def __move_to_free_spot(self, city: City) -> None:
        current_location = self.get_location()
        next_position_list = city.find_free_spot(current_location)
        next_position = random.choice(next_position_list)

        city.set_agent("SurviviorBot", next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

    def __pick_up(self):
        # See if there is a spare part in your view
        # Go to the spare part (Replace Spare Part grid with Survivor_bot)
        # Add Spare part to the inventory
        # go to the nearest Recharge Station
        pass



