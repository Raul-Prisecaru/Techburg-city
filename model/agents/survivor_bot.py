import os

from abc import ABC
import random
from typing import List, Optional

from model.agents.spare_part import SparePart
from model.recharge_station import RechargeStation
from model.city import City
from model.agent import Agent
from model.location import Location
current_dir = os.path.dirname(__file__)
move_up_dir = os.path.dirname(current_dir)


class SurvivorBot(Agent):
    def __init__(self, location: Location) -> None:
        """
        Constructor to configure default values upon created

            Parameter:
                location (Location): Starting Location of the Survivor Bot

        """
        super().__init__(location)
        # Inventory System. Only one slot available
        self.__inventory = []
        self.__energy = 100
        self.__no_energy_turn = 0

        self.__enhancements = {
            "speed":  0,
            "vision": 0,
            "energy": 0
        }

        self.__incident = {
            # if Attacked, should probably focus on speed enhancement
            "attacked": 0,

            # if encountered drone, should probably focus on vision enhancement
            "drone-encounter": 0,

            # if ran out of energy in the field, should probably focus on energy enhancement
            "out-of-energy": 0
        }

        self.__recharge_station: RechargeStation = None

    def act(self, city: City) -> None:
        """
        Function responsible for handling the logic of actions the survivor bot can execute

            Parameter:
                city (City): Environment where actions can be executed

            Return:
                None

        """

        available_free_spots = city.find_free_spot(self.get_location())
        available_sparePart  = city.find_spare_part(self.get_location())
        danger_list = city.find_danger_nearby(self.get_location())


        while True:

            # If Survivor Bot has Energy
            if self.__energy > 0:

                # If you are in danger
                if (len(danger_list)) > 0:

                    # Go back to Recharge Station
                    self.__move_to_recharge_station(city)
                    break

                # If you have a spare part in your inventory
                if len(self.__inventory) > 0:

                    # Go To Recharge Station
                    self.__move_to_recharge_station(city)
                    break

                # if there is a spare part in your vision
                if len(available_sparePart) > 0:

                    # Move Towards the Spare Part and Pick it up
                    self.__pick_up_spare_part(city, available_sparePart)
                    break

                # if there is a free spot in your vision
                if len(available_free_spots):

                    # Check Against the memory to see which location you haven't travelled

                    # Move towards that free spot
                    self.__move_to_free_spot(city, available_free_spots)
                    break

            # If energy is lower or equals to 0
            if self.__energy <= 0:
                # Check inventory if there is a spare part
                if len(self.__inventory):

                    # Consume Spare Part
                    self.__consume_spare_part(self.__inventory)
                    break

                else:
                    # If no energy turns is less than 9
                    if self.__no_energy_turn < 9:
                        # Tracking amount of turns of no energy
                        self.__no_energy_turn += 1
                        pass

                    else:
                        self.__removed_from_grid(city)
                pass

    def __move_to_free_spot(self, city: City, available_freeSpots: List[Location]) -> None:
        """
        Function to allow Survivor bot to travel to a free available cell

            Parameters:
                city (City): Environment to execute movement

            Returns:
                None

        """

        next_position = random.choice(available_freeSpots)


        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, self.get_location())

        self.__energy -= 5



    def __pick_up_spare_part(self, city: City, available_spareParts: List[Location]) -> None:
        """
        Function that allows the survivor bot to move to a spot where Spare Part is located

            Parameter:
                city (City): Environment to execute movement

            Returns:
                None
        """


        next_position = random.choice(available_spareParts)

        self.__inventory.append(city.get_agent(next_position))

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, self.get_location())

        self.__energy -= 5


    def __move_to_recharge_station(self, city: City) -> None:
        """
        Function that is responsible for handling logic of moving the survivor bot closer towards the recharge Station

            Parameter:
                city (City): Environment to execute movement

            Return:
                None
        """

        next_move_station = city.find_next_move_recharge_station(self.get_location(), self.__recharge_station.get_location())


        # Checking if the next move is at the Recharge Station Location
        if next_move_station.get_x() == self.__recharge_station.get_location().get_x() and next_move_station.get_y() == self.__recharge_station.get_location().get_y():
            city.set_agent(None, self.get_location())
            self.__recharge_station.add_survivor_bot(self)

            if len(self.__inventory) > 0:
                self.__recharge_station.add_spare_part(self.__inventory[0])

        else:
            city.set_agent(self, next_move_station)
            self.set_location(next_move_station)
            city.set_agent(None, self.get_location())


    def get_inventory(self) -> Optional[List[SparePart]]:
        """
        Function responsible for retrieving the inventory of the survivor bot

            Parameter:
                None

            Return:
                Optional[List[SparePart]] -> Returns the inventory which may contain a singular Spare Part or None
        """
        return self.__inventory


    def get_energy(self) -> int:
        """
        Function responsible for retrieving the current Energy Status of the Survivor Bot

            Parameter:
                None

            Return:
                int: Current Percentage remaining of the survivor bot's energy
        """
        return self.__energy


    def set_energy(self, new_energy: int) -> None:
        """
        Function responsible for overriding the current Energy Status of the survivor bot

            Parameter:
                new_energy (int): New energy value to override the current energy status with

            Return:
                None
        """

        self.__energy = new_energy

    def __danger_nearby(self):
        pass

    def __removed_from_grid(self, city: City) -> None:
        """
        Function responsible for removing the survivor bot from the environment

            Parameter:
                city (City): Environment to remove survivor bot

            Return:
                None

        """
        city.set_agent(None, self.get_location())


    def __does_robot_enough_energy_back(self, go_back_location: Location) -> bool:
        """
        Function responsible for calculating if survivor bot has enough energy to a specified Location

            Parameter:
                go_back_location (Location): Location to compare against

            Return:
                bool: Returns TRUE if survivor can make it back between two location else returns FALSE
        """
        total_distance_station = abs(self.get_location().get_x() - go_back_location.get_x()) + abs(self.get_location().get_y() - go_back_location.get_y())

        total_distance = total_distance_station * 2

        total_energy_required = total_distance * 5

        if self.__energy > total_energy_required:
            return True

        if self.__energy < total_energy_required:
            return False

    def __consume_spare_part(self, inventory: List[SparePart]) -> None:
        """
        function responsible managing survivor bot consuming Spare Parts from inventory
            Parameters:
                inventory (List[SparePart]): Inventory to take out spare part if available

            Return:
                None
        """

        inventory.clear()

        # TODO: Improve this so instead of setting to 100, it takes into consideration it's enhancement.
        self.__energy = 100


    def get_energy_turn(self) -> int:
        """
        Function responsible for retrieving the number of turns survivor bot went without energy

            Parameter:
                None

            Return:
                int: Number of turns survivor bot went without energy
        """
        return self.__no_energy_turn

    def get_speed_enhancement(self) -> int:
        """
        Function responsible for retrieving the survivor bot current Speed enhancement percentage

            Parameter:
                None

            Return:
                int: Survivor Bot's current Speed enhancement Percentage
        """
        return self.__enhancements["speed"]

    def get_vision_enhancement(self) -> int:
        """
        Function responsible for retrieving the survivor bot current Vision enhancement percentage

            Parameter:
                None

            Return:
                int: Survivor Bot's current Vision enhancement Percentage
        """
        return self.__enhancements["vision"]

    def get_energy_enhancement(self) -> int:
        """
        Function responsible for retrieving the survivor bot current energy enhancement percentage

        Parameter:
            None

        Return:
            int: Survivor Bot's current energy enhancement Percentage
        """
        return self.__enhancements["energy"]



    def increase_speed(self, increase_by: int) -> None:
        """
        Function responsible for increasing the survivor bot current speed enchantment
            Parameter:
                increase_by (int): Increase survivor bot current speed by

            Return:
                None
        """
        current_speed = self.__enhancements["speed"]
        self.__enhancements.update({"speed": current_speed + increase_by})

    def increase_vision(self, increase_by: int) -> None:
        """
        Function responsible for increasing the survivor bot current vision enchantment
            Parameter:
                increase_by (int): Increase survivor bot current vision by

            Return:
                None
        """
        current_vision = self.__enhancements["vision"]
        self.__enhancements.update({"vision": current_vision + increase_by})

    def increase_energy(self, increase_by) -> None:
        """
        Function responsible for increasing the survivor bot current energy enchantment
            Parameter:
                increase_by (int): Increase survivor bot current energy by

        Return:
            None
        """
        current_energy = self.__enhancements["energy"]
        self.__enhancements.update({"energy": current_energy + increase_by})

    def set_primary_recharge_station(self, recharge_station: RechargeStation):
        """
        Function responsible for setting the default recharge station for the survivor bot

            Parameter:
                recharge_station (RechargeStation): default Recharge Station for the Survivor Bot

            Return:
                None
        """
        self.__recharge_station = recharge_station




# Use Genetic Algorithm to determine how many Agents should be added by seeing which longest simulation is running
# Measured in Steps ^^
# ^^ Advanced