from __future__ import annotations

from abc import ABC

from model.environment import Environment
from model.location import Location
from model.agent import Agent
from typing import override, Optional, List, TYPE_CHECKING, Union
from model.agents.spare_part import SparePart

from model.agents.malfunctioning_drone import MalfunctioningDrone
# Importing these files if they are being used for Type_checking
# Helps to avoid circular Imports
if TYPE_CHECKING:
    from agents.survivor_bot import SurvivorBot
    from agents.scavenger_swarm import ScavengerSwarm



class City(Environment, ABC):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)

        # Environment
        self.__environment: List[Union[object, None]] = []

        self.__height = height
        self.__width = width

        # Creating Grid with for loop based on provided width and heights
        for _ in range(self.__height):
            self.__environment.append([None] * self.__width)

    # Returns an Agent if found at provided location else None
    def get_agent(self, location: Location) -> Optional[Agent]:
        return self.__environment[location.get_y()][location.get_x()]

    # Sets an Agent at provided location.
    def set_agent(self, agent: Optional[Agent], location: Location) -> None:
        self.__environment[location.get_y()][location.get_x()] = agent

    # Function to Find free available spots around the location provided
    def find_free_spot(self, location: Location) -> List[Location]:
        # "Coordinates" to indicate where to search for free spots
        # Implement logic to check for bot's status and apply appropriate offsets

        free_spots: List[Location] = []

        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # For Loop to check for Free Space
        for offset_x, offset_y in normal_offsets:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = (location.get_x() + offset_x) % self.__width
            new_offset_y = (location.get_y() + offset_y) % self.__height

            # Checking if there is something at those new coordinates
            if self.__environment[new_offset_y][new_offset_x] is None:
                free_spots.append(Location(new_offset_y, new_offset_x))

        return free_spots

    def find_spare_part(self, location: Location) -> List[Location]:
        # "Coordinates" to indicate where to search for free spots
        # Implement logic to check for bot's status and apply appropriate offsets

        spare_parts: List[Location] = []

        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]



        # For Loop to check for Free Space
        for offset_x, offset_y in normal_offsets:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = (location.get_x() + offset_x) % self.__width
            new_offset_y = (location.get_y() + offset_y) % self.__height

            if isinstance(self.__environment[new_offset_y][new_offset_x], SparePart):
                spare_parts.append(Location(new_offset_y, new_offset_x))


        return spare_parts

    def find_next_move_recharge_station(self, current_location: Location, recharge_location: Location) -> Location:
        next_move_x = None
        next_move_y = None

        if current_location.get_x() > recharge_location.get_x():
            next_move_x = current_location.get_x() - 1

        if current_location.get_x() < recharge_location.get_x():
            next_move_x = current_location.get_x() + 1

        else: next_move_x = current_location.get_x()

        if current_location.get_y() > recharge_location.get_y():
            next_move_y = current_location.get_y() - 1

        if current_location.get_y() < recharge_location.get_y():
            next_move_y = current_location.get_y() + 1

        else: next_move_y = current_location.get_y()

        return Location(next_move_y, next_move_x)

    # TODO: Fix: MalfunctioningDrone is not undefined
    def find_danger_nearby(self, location: Location) -> List[Location]:
        # "Coordinates" to indicate where to search for free spots
        # Implement logic to check for bot's status and apply appropriate offsets

        danger_nearby: List[Location] = []
        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # For Loop to check for Free Space
        for offset_x, offset_y in normal_offsets:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = (location.get_x() + offset_x) % self.__width
            new_offset_y = (location.get_y() + offset_y) % self.__height

            # Checking if there is something at those new coordinates
            if self.__environment[new_offset_y][new_offset_x] is MalfunctioningDrone:
                danger_nearby.append(Location(new_offset_y, new_offset_x))

        # return self.__free_spots, self.__survivor_bot_nearby, self.__malfunctioning_drone_nearby, self.__scavenger_swarm_nearby, self.__spare_part_nearby
        return danger_nearby



    # Display Environment
    def display_environment(self):
        for row in range(self.__height):
            print(self.__environment[row])


    def check_space_if_None(self, location: Location) -> bool:
        if self.__environment[location.get_y()][location.get_x()] is None:
            return True
        else:
            return False


    def add_objects_to_map(self, list_Location: List[Location], object_toAdd: object):
        for location in list_Location:
            self.__environment[location.get_y()][location.get_x()] = object_toAdd

