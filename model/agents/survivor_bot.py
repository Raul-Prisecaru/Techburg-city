import os

from abc import ABC
import random
from typing import List

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
        Constructor to set the default values

        :param location: Sets the location of the survivor bot

        :var self.__inventory: Acts as an inventory system allowing survivor bot to hold spare parts

        :var self.__energy --> Energy System determining how far survivor_bot can travel

        :var self.__no_energy_turn --> Keeps track of how many turns has been when survivor bot has no energy

        :dict self.__enhancements --> Responsible for keeping track of any enhancement made

        :dict self.__incident --> Responsible for keeping track of any incident to this survivor bot which will be used to better strategy on what enhancement to be made
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
        Function that allows the survivor bot to execute actions

        :param city --> city environment where survivor bot can execute actions on

        :param recharge_station --> recharge object used to get it's current location (Temporarily)

        """
        current_location = self.get_location()

        available_free_spots = city.find_free_spot(current_location)
        available_sparePart  = city.find_spare_part(current_location)
        danger_list = city.find_danger_nearby(current_location)

        while True:

            # If Survivor Bot has Energy
            if self.__energy > 0:

                # If you are in danger
                if (len(danger_list)) > 0:

                    # Go back to Recharge Station
                    self.__move_to_recharge_station()
                    pass

                # If you have a spare part in your inventory
                if len(self.__inventory) > 0:

                    # Go To Recharge Station
                    self.__move_to_recharge_station()
                    pass

                # if there is a spare part in your vision
                if len(sparePart_list) > 0:

                    # Move Towards the Spare Part and Pick it up
                    self.__pick_up_spare_part()
                    pass

                # if there is a free spot in your vision
                if len(freeSpot_list):

                    # Check Against the memory to see which location you haven't travelled

                    # Move towards that free spot
                    self.__move_to_free_spot()
                    pass

                # if the next move at the recharge station Location:
                if ():
                    pass

            # If energy is lower or equals to 0
            if self.__energy <= 0:
                # Check inventory if there is a spare part
                if len(self.__inventory):

                    # Consume Spare Part
                    self.__attempt_consume_part()

                else:
                    # If no energy turns is less than 10
                    if self.__no_energy_turn < 9:
                        # Tracking amount of turns of no energy
                        self.__no_energy_turn += 1
                        pass

                    else:
                        self.__removed_from_grid()
                pass



            # if (self.__does_robot_enough_energy_back(current_location, self.__recharge_station.get_location()) == False) and self.__energy < 5:
            #     self.__attempt_consume_part(self.__inventory)
            #     pass
            # if self.__energy > 0:
            #     if len(self.__inventory) > 0:
            #         self.__go_to_recharge_station(city, current_location, next_move_station, self.__recharge_station)
            #         break
            #
            #     if len(sparePart_list) != 0:
            #         self.__pick_up_spare_part(city, current_location, sparePart_list)
            #         break
            #
            #     if len(freeSpot_list) != 0:
            #         self.__move_to_free_spot(city, current_location, freeSpot_list)
            #         break
            #
            # elif self.__energy == 0:
            #     print("I have no energy left")
            #     self.__no_energy_turn += 1
            #
            #     if self.__no_energy_turn >= 5:
            #         self.__removed_from_grid(city, current_location)
            #         break
            #     break
    def __move_to_free_spot(self, city: City, current_location: Location, available_freeSpots: List[Location]) -> None:
        """
        Function to allow Survivor bot to travel to a free available cell

            Parameters:
                city (City): Environment to execute movement

                currentLocation (Location): Used to find nearby free spots

            Returns:
                None

        """

        next_position = random.choice(available_freeSpots)


        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

        self.__energy -= 5



    def __pick_up_spare_part(self, city: City, current_location: Location, available_spareParts: List[Location]) -> None:
        """
        Function that allows the survivor bot to move to a spot where Spare Part is located

            Parameter:
                city (City): Environment to execute movement

                currentLocation (Location): Used to find nearby Spare Part

            Returns:
                None
        """


        next_position = random.choice(available_spareParts)

        self.__inventory.append(city.get_agent(next_position))

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

        self.__energy -= 5


    def __insert_into_recharge_station(self):
        """
        Function is resposible for handling logic of inserting the Survivor Bot into the recharge Station
        :return:
        """
        pass

    def __move_to_recharge_station(self, city: City, current_location: Location) -> None:
        """
        Function that is responsible for handling logic of moving the survivor bot closer towards the recharge Station

            Parameter:
                city (City): Environment to execute movement

                current_Location (Location): Used to find the best location to the Recharge Station from it's current Location

        """

        next_move_station = city.find_next_move_recharge_station(current_location, self.__recharge_station.get_location())

        city.set_agent(self, next_move_station)
        self.set_location(next_move_station)
        city.set_agent(None, current_location)


    def get_inventory(self) -> List[SparePart]:
        """
        Function to retrieve the inventory of the survivor bot. May contain a singular spare part or be an empty list
        :return: --> The current Inventory of the survivor bot
        """
        return self.__inventory


    def get_energy(self) -> int:
        """
        Function to retrieve the current Energy Status of the survivor bot
        :return: --> The current Energy Status of the survivor bot
        """
        return self.__energy


    def set_energy(self, new_energy: int) -> None:
        """

        :param new_energy: Value to set the new energy
        :return: None
        """
        self.__energy = new_energy

    def __danger_nearby(self):
        pass

    def __removed_from_grid(self, city: City, current_location: Location) -> None:
        """
        Function to remove survivor bot from the environment if certain conditions meet
        :param city: --> Environment to remove Survivor Bot from
        :param current_location --> Current Location of the Survivor Bot
        :return --> Returns None
        """
        city.set_agent(None, current_location)


    def __does_robot_enough_energy_back(self, current_location: Location, go_back_location: Location) -> bool:
        """
        function to calculate if Survivor bot has enough energy to travel back to specified location (Typically used for Recharge Station)

        :param current_location --> Current Location of the Survivor Bot
        :param: go_back_location --> Location to calculate the distance between
        :return: --> Returns True if Survivor bot has enough energy else Returns False if Survivor bot does not have enough energy
        """
        total_distance_station = abs(current_location.get_x() - go_back_location.get_x()) + abs(current_location.get_y() - go_back_location.get_y())

        total_distance = total_distance_station * 2

        total_energy_required = total_distance * 5

        if self.__energy > total_energy_required:
            return True

        if self.__energy < total_energy_required:
            return False

    def __attempt_consume_part(self, inventory: List[SparePart]) -> None:
        """
        function to allow the survivor bot to attempt at consuming a Spare Part
        :param inventory --> Inventory of the survivor bot
        :return: --> Returns None
        """

        if len(inventory) > 0:
            inventory.clear()
            self.__energy = 100
        else:
            print("I do not have spare part in my inventory to consume")


    def get_energy_turn(self) -> int:
        return self.__no_energy_turn

    def get_speed_enhancement(self) -> int:
        return self.__enhancements["speed"]

    def get_vision_enhancement(self) -> int:
        return self.__enhancements["vision"]

    def get_energy_enhancement(self) -> int:
        return self.__enhancements["energy"]



    def increase_speed(self, increase_by: int) -> None:
        current_speed = self.__enhancements["speed"]
        self.__enhancements.update({"speed": current_speed + increase_by})

    def increase_vision(self, increase_by: int) -> None:
        current_vision = self.__enhancements["vision"]
        self.__enhancements.update({"vision": current_vision + increase_by})

    def increase_energy(self, increase_by) -> None:
        current_energy = self.__enhancements["energy"]
        self.__enhancements.update({"energy": current_energy + increase_by})

    def set_primary_recharge_station(self, recharge_station: RechargeStation):
        self.__recharge_station = recharge_station




# Use Genetic Algorithm to determine how many Agents should be added by seeing which longest simulation is running
# ^^ Advanced