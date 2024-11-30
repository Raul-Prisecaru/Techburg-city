from __future__ import annotations

from abc import ABC

from model.environment import Environment
from model.location import Location
from model.agent import Agent
from typing import override, Optional, List, TYPE_CHECKING
from model.agents.spare_part import SparePart

# Importing these files if they are being used for Type_checking
# Helps to avoid circular Imports
if TYPE_CHECKING:
    from agents.survivor_bot import SurvivorBot
    from agents.malfunctioning_drone import MalfunctioningDrone
    from agents.scavenger_swarm import ScavengerSwarm



class City(Environment, ABC):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        # Environment where everything happens
        self.__environment = []
        # Storing Free available spaces
        self.__free_spots = []
        # Storing the coordinates of nearby Survivor Bot
        self.__survivor_bot_nearby = []
        # Storing the coordinates of nearby Drones
        self.__malfunctioning_drone_nearby = []
        # Storing the coordinates of nearby Scavenger Swarms
        self.__scavenger_swarm_nearby = []
        # Storing the coordinates of nearby Spare Part
        self.__spare_part_nearby = []

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
        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),  (0, 0),  (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # For Loop to check for Free Space
        for offset_x, offset_y in normal_offsets:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = location.get_x() + offset_x
            new_offset_y = location.get_y() + offset_y

            # Checking if there is something at those new coordinates
            if self.__environment[new_offset_y][new_offset_x] is None:
                self.__free_spots.append(Location(new_offset_y, new_offset_x))

        # return self.__free_spots, self.__survivor_bot_nearby, self.__malfunctioning_drone_nearby, self.__scavenger_swarm_nearby, self.__spare_part_nearby
        return self.__free_spots

    def find_spare_part(self, location: Location) -> List[Location]:
        # "Coordinates" to indicate where to search for free spots
        # Implement logic to check for bot's status and apply appropriate offsets
        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),  (0, 0),  (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]



        # For Loop to check for Free Space
        for offset_x, offset_y in normal_offsets:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = location.get_x() + offset_x
            new_offset_y = location.get_y() + offset_y

            if isinstance(self.__environment[new_offset_y][new_offset_x], SparePart):
                print("There is a spare part in my radius")
                self.__spare_part_nearby.append(Location(new_offset_y, new_offset_x))


        return self.__spare_part_nearby

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









    # Display Environment
    def display_environment(self):
        for row in range(self.__height):
            print(self.__environment[row])


    def check_space_if_None(self, location: Location) -> bool:
        if self.__environment[location.get_x()][location.get_y()] is None:
            return True
        else:
            return False


    def add_objects_to_map(self, list_Location: List[Location], object_toAdd: Agent):
        for location in list_Location:
            self.__environment[location.get_y()][location.get_x()] = object_toAdd

