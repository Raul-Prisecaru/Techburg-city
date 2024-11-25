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

        :var self.__No_energy_turn --> Keeps track of how many turns has been when survivor bot has no energy

        :dict self.__enhancements --> Responsible for keeping track of any enhancement made

        :dict self.__incident --> Responsible for keeping track of any incident to this survivor bot which will be used to better strategy on what enhancement to be made
        """
        super().__init__(location)
        # Inventory System. Only one slot available
        self.__inventory = []
        self.__energy = 100
        self.__No_energy_turn = 0

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

        :var current_location --> Gets the current location of the survivor bot

        :var sparePart_list --> Checks around for any spare part from the current location and returns a list of Locations if found

        :var freeSpot_list --> Checks around for any free spots from the current location and returns a list of Locations if found

        :var next_move_station --> finds best next coordinate to travel to the recharge station

        """
        current_location = self.get_location()

        sparePart_list = city.find_spare_part(current_location)
        freeSpot_list = city.find_free_spot(current_location)
        print("Recharge Station Location, ", self.__recharge_station.get_location())
        next_move_station = city.find_next_move_recharge_station(current_location, self.__recharge_station.get_location())


        while True:

            if (self.__does_robot_enough_energy_back(city, current_location, self.__recharge_station.get_location()) == False) and self.__energy < 5:
                self.__attempt_consume_part(self.__inventory)
                pass
            if self.__energy > 0:
                if len(self.__inventory) > 0:
                    self.__go_to_recharge_station(city, current_location, next_move_station, self.__recharge_station)
                    break

                if len(sparePart_list) != 0:
                    self.__pick_up_spare_part(city, current_location, sparePart_list)
                    break

                if len(freeSpot_list) != 0:
                    self.__move_to_free_spot(city, current_location, freeSpot_list)
                    break

            else:
                print("I have no energy left")
                self.__No_energy_turn += 1

                if self.__No_energy_turn >= 10:
                    self.__removed_from_grid(city, current_location)

    def __move_to_free_spot(self, city: City, current_location: Location, location_list: List[Location]) -> None:
        """
        Function that allows the survivor bot to move to a free spot

        :param city --> Used to move the survivor bot to the new location and remove from it's previous location

        :param current_location -->  Used to set it's previous location to None to avoid duplicates

        :param location_list --> List of Free Locations

        :var self.__energy --> Used to reduce survivor bot energy after moving
        """
        next_position = random.choice(location_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)
        self.__energy -= 5



    def __pick_up_spare_part(self, city: City, current_location: Location, location_list: List[Location]) -> None:
        """
        Function that allows the survivor bot to move to a spot where Spare Part is located

        :param city --> Used to move the survivor bot to the new location and remove from it's previous location

        :param current_location --> Used to set it's previous location to None to avoid duplicates

        :param location_list --> List of spare parts Locations

        """

        # Go to the spare part (Replace Spare Part grid with Survivor_bot)
        if len(self.__inventory) == 0:
            random_part = random.choice(location_list)
            self.__inventory.append(city.get_agent(random_part))

            city.set_agent(self, random_part)

            self.set_location(random_part)

            city.set_agent(None, current_location)

            # Add Spare part to the inventory
            print("I have picked up an Spare Part!")



    def __go_to_recharge_station(self, city: City, current_location: Location, next_move: Location, recharge_station: RechargeStation) -> None:
        """
        Function that is responsible for moving the survivor bot to the recharge station
        and insert the survivor bot and spare part into the recharge station

        :param city --> Used to move the survivor bot to the new location and remove from it's previous location

        :param current_location --> Used to set it's previous location to None to avoid duplicates

        :param next_move --> Next closest position to the recharge station from survivor bot current position

        :param recharge_station --> recharge station to go to and insert the survivor bot into alongside with it's spare part

        """


        if next_move.get_x() == Location(15, 29).get_x() and next_move.get_y() == Location(15, 29).get_y():
            city.set_agent(None, current_location)
            recharge_station.add_survivor_bot(self)
            recharge_station.add_spare_part(self.__inventory[0])
            print(recharge_station.get_survivor_bot())
            print(recharge_station.get_spare_part())

            self.__inventory.clear()

        else:
            city.set_agent(self, next_move)
            self.set_location(next_move)
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
            inventory.pop()
            self.__energy = 100
        else:
            print("I do not have spare part in my inventory to consume")



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