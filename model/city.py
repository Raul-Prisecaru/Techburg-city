from abc import ABC

from environment import Environment
from location import Location
from agent import Agent
from typing import override, Optional, List
from agents.survivor_bot import SurvivorBot


class City(Environment, ABC):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self.__environment = []
        self.__free_spots = []
        self.__robot_nearby = []
        self.__drones_nearby = []
        self.__nanobots_nearby = []
        self.__spare_part_nearby = []

        for _ in range(height):
            self.__environment.append([None] * width)

    def get_agent(self, location: Location) -> Optional[Agent]:
        return self.__environment[location.get_x()][location.get_y()]

    def set_agent(self, agent: Agent, location: Location) -> None:
        self.__environment[location.get_x()][location.get_y()] = agent


    def find_free_spot(self, location: Location) -> List[Location]:
        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),  (0, 0),  (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for offset_x, offset_y in normal_offsets:

            new_offset_x = location.get_x() + offset_x
            new_offset_y = location.get_y() + offset_y

            if self.__environment[new_offset_x][new_offset_y] is None:
                self.__free_spots.append(Location(new_offset_x, new_offset_y))

            if self.__environment[new_offset_x][new_offset_y] is SurvivorBot:
                self.__robot_nearby.append(Location(new_offset_x, new_offset_y))


