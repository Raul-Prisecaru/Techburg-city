import os

from abc import ABC
import random
from typing import List
from model.recharge_station import RechargeStation
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
    # Implement a function to act as a enchacement status of the bot
    # Perhaps use a Dict to have the enchancment name : percentage?
    # e.g speed : 50%
    # TODO: As a reminder to see this above

    # This will basically act like a priority List
    # In will do the most important thing first to last
    # e.g First check for enemies around, second check for spare part
    # Might be something like this in order:
    """
    Priority list (In order)
    - Check for enemies (drones / nanobots) around -> Run away to nearest recharge station
    - Check for spare part around -> Pick up and go to nearest recharge station
    - Go to unexplored cell -> Pick random if multiple
    - Go to an explorered cell if all cells were explored around it -> Pick random if multiple
    """
    def act(self, city: City) -> None:
        current_location = self.get_location()

        sparePart_list = city.find_spare_part(current_location)
        freeSpot_list = city.find_free_spot(current_location)
        next_move_station = city.find_next_move_recharge_station(current_location, Location(15, 29))


        while True:

            if len(self.__inventory) > 0:
                self.__go_to_recharge_station(city, current_location, next_move_station)
                break

            if len(sparePart_list) != 0:
                self.__pick_up_spare_part(city, current_location, sparePart_list)
                break

            if len(freeSpot_list) != 0:
                self.__move_to_free_spot(city, current_location, freeSpot_list)
                break

    def __move_to_free_spot(self, city: City, current_location: Location, location_list: List[Location]) -> None:
        next_position = random.choice(location_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

    def __pick_up_spare_part(self, city: City, current_location: Location, location_list: List[Location]) -> None:
        # Go to the spare part (Replace Spare Part grid with Survivor_bot)
        if len(self.__inventory) == 0:
            random_part = random.choice(location_list)
            self.__inventory.append(city.get_agent(random_part))

            city.set_agent(self, random_part)

            self.set_location(random_part)

            city.set_agent(None, current_location)

            # Add Spare part to the inventory
            print("I have picked up an Spare Part!")



    def __go_to_recharge_station(self, city: City, current_location: Location, next_move: Location):
        city.set_agent(self, next_move)
        self.set_location(next_move)
        city.set_agent(None, current_location)


    def get_inventory(self):
        return self.__inventory




