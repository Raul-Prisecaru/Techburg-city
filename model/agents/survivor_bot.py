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
        # If this returns True
        if self.__pick_up_spare_part(city):
            # Code to go to the nearest Recharge Station
            pass
        self.__move_to_free_spot(city)

    def __move_to_free_spot(self, city: City) -> None:
        current_location = self.get_location()
        next_position_list = city.find_free_spot(current_location)
        next_position = random.choice(next_position_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

    def __pick_up_spare_part(self, city: City) -> bool:
        # See if there is a spare part in your view
        current_location = self.get_location()
        spare_part_nearby_list = city.find_spare_part(current_location)

        # Go to the spare part (Replace Spare Part grid with Survivor_bot)
        if len(spare_part_nearby_list) != 0:
            if len(self.__inventory) == 0:
                random_part = random.choice(spare_part_nearby_list)
                city.set_agent(self, random_part)
                # Add Spare part to the inventory
                self.__inventory.append(city.get_agent(random_part))
                print("I have picked up an Spare Part!")
                print("This is now my inventory: ",  self.__inventory)
                return True

            else:
                return False
        else:
            return False



    def __go_to_recharge_station(self):
        pass

    def get_inventory(self):
        return self.__inventory




