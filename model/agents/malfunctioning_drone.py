from __future__ import annotations

import os
from abc import ABC
import random
from typing import TYPE_CHECKING, List

from model.agent import Agent
from model.location import Location
current_dir = os.path.dirname(__file__)
move_up_dir = os.path.dirname(current_dir)

if TYPE_CHECKING:
    from model.city import City



class MalfunctioningDrone(Agent):
    def __init__(self, location: Location):
        super().__init__(location)
        self.__energy = 100

        self.__free_position_list: List[Location] = []
        self.__survivor_bot_list: List[Location] = []



    def act(self, city: City) -> None:
        """
        Function responsible for handling the logic of the Malfunctioning Drone

            Parameter:
                city (City): Environment where actions can be executed

            Return:
                None

        """
        self.__free_position_list = city.find_free_spot(self.get_location())
        # self.__survivor_bot_list = city.find_survivor_bot(self.get_location())
        while True:
            if self.__energy <= 20:
                self.__hibernate()
                break

            if len(self.__survivor_bot_list) > 0:
                self.__move_towards_survivor_bot(city)
                break

            if len(self.__free_position_list) > 0:
                self.__move(city)
                break



    def __move(self, city: City) -> None:
        """
        Function responsible for moving the malfunctioning drone to a free spot

            Parameter:
                city (City): environment to move around

            Return:
                None

        """

        previous_location: Location = self.get_location()

        next_position: Location = random.choice(self.__free_position_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, previous_location)

        self.__energy -= 5



    def __move_towards_survivor_bot(self, city: City) -> None:
        """
        Function responsible for allowing the malfunctioning drone to chase after survivor bot

            Parameter:
                - city (city): environment to move around

            Return:
                - None
        """



        current_location: Location = self.get_location()

        next_position: Location = random.choice(self.__survivor_bot_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)

        self.__energy -= 20


    def get_energy(self) -> int:
        """
        Function responsible for returning current energy status

            Parameter:
                None

            Return:
                None
        """
        return self.__energy


    def set_energy(self, new_energy: int) -> None:
        """
        Function responsible for overriding the current energy status

            Parameter:
                None

            Return:
                None
        """

        self.__energy = new_energy


    def __hibernate(self) -> None:
        """
        Function responsible for allowing the malfunction drone to hibernate and gain 10% energy

            Parameter:
                None

            Return:
                  None

        """

        # TODO: Perhaps introduce an Priority system to ensure that the Drone keeps hibernating till max charge

        self.__energy += 10



