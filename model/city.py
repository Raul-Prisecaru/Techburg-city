from abc import ABC

from model.environment import Environment
from model.location import Location
from model.agent import Agent
from typing import override, Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from agents.survivor_bot import SurvivorBot
    from agents.malfunctioning_drone import MalfunctioningDrone
    from agents.scavenger_swarm import ScavengerSwarm
    from agents.spare_part import SparePart


class City(Environment, ABC):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self.__environment = []
        self.__free_spots = []
        self.__survivor_bot_nearby = []
        self.__malfunctioning_drone_nearby = []
        self.__scavenger_swarm_nearby = []
        self.__spare_part_nearby = []
        self.__height = height

        for _ in range(height):
            self.__environment.append([None] * width)

    def get_agent(self, location: Location) -> Optional[Agent]:
        return self.__environment[location.get_x()][location.get_y()]

    def set_agent(self, agent: Agent, location: Location) -> None:
        self.__environment[location.get_x()][location.get_y()] = agent


    def find_free_spot(self, location: Location):
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
                self.__survivor_bot_nearby.append(Location(new_offset_x, new_offset_y))

            if self.__environment[new_offset_x][new_offset_y] is MalfunctioningDrone:
                self.__malfunctioning_drone_nearby.append(Location(new_offset_x, new_offset_y))

            if self.__environment[new_offset_x][new_offset_y] is ScavengerSwarm:
                self.__scavenger_swarm_nearby.append(Location(new_offset_x, new_offset_y))

            if self.__environment[new_offset_x][new_offset_y] is SparePart:
                self.__spare_part_nearby.append(Location(new_offset_x, new_offset_y))


        # return self.__free_spots, self.__survivor_bot_nearby, self.__malfunctioning_drone_nearby, self.__scavenger_swarm_nearby, self.__spare_part_nearby
        return self.__free_spots


    def display_environment(self):
        for row in range(self.__height):
            print(self.__environment[row])

