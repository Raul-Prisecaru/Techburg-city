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

        self.__survivor_bot_list: List[Location] = []



    def act(self, city: City) -> None:

        self.__survivor_bot_list = city.find_survivor_bot(self.get_location())

        if len(self.__survivor_bot_list) > 0:
            self.__move_towards_survivor_bot(city)

        self.__move(city)

    def __move(self, city: City) -> None:
        previous_location: Location = self.get_location()
        next_position_list = city.find_free_spot(previous_location)
        next_position: Location = random.choice(next_position_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, previous_location)


    def __move_towards_survivor_bot(self, city: City) -> None:
        current_location: Location = self.get_location()

        next_position: Location = random.choice(self.__survivor_bot_list)

        city.set_agent(self, next_position)

        self.set_location(next_position)

        city.set_agent(None, current_location)





