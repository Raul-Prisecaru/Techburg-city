from __future__ import annotations

from abc import ABC

from model.environment import Environment
from model.location import Location
from model.agent import Agent
from typing import Optional, List, TYPE_CHECKING, Union
from model.agents.spare_part import SparePart
from model.retrieve_offset import RetrieveOffset

from model.agents.malfunctioning_drone import MalfunctioningDrone

# Importing these files if they are being used for Type_checking
# Helps to avoid circular Imports
if TYPE_CHECKING:
    from agents.scavenger_swarm import ScavengerSwarm


# TODO: Optimise off_sets to avoid repeating over and over and to take into consideration bot's enhancement
class City(Environment, ABC):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self.__retrieveOffset = RetrieveOffset()

        # Environment
        self.__environment: List[Union[object, None]] = []

        self.__height = height
        self.__width = width

        # Creating Grid with for loop based on provided width and heights
        for _ in range(self.__height):
            self.__environment.append([None] * self.__width)

        vision_1_cells = []
        vision_2_cells = []
        vision_3_cells = []
        for x in range(-3, 4):
            for y in range(-3, 4):
                vision_3_cells.append((x, y))

        for x in range(-2, 3):
            for y in range(-2, 3):
                vision_2_cells.append((x, y))

        for x in range(-1, 2):
            for y in range(-1, 2):
                vision_1_cells.append((x, y))

        self.__retrieveOffset.add_rule_for_vision_enhancement(lambda x: x <= 50, vision_1_cells)
        self.__retrieveOffset.add_rule_for_vision_enhancement(lambda x: 51 <= x <= 100, vision_2_cells)
        self.__retrieveOffset.add_rule_for_vision_enhancement(lambda x: 101<=x <= 150, vision_3_cells)

    def get_agent(self, location: Location) -> Optional[Agent]:
        """
        Function Responsible for returning the agent found at specified Location
            Parameter:
                location (Location): Location to check for agent

            Result:
                Agent: Returns an Agent if found else None
        """
        return self.__environment[location.get_y()][location.get_x()]

    def set_agent(self, agent: Optional[Agent], location: Location) -> None:
        """
        Function Responsible for adding agent to specified location
            Parameter:
                agent (Agent): Agent to add
                location (Location): Location to add the agent to

            Result:
                None
        """

        # TODO: Add check to ensure we do not override
        self.__environment[location.get_y()][location.get_x()] = agent

    def find_free_spot(self, location: Location) -> List[Location]:
        """
        Function Responsible for finding free spot from specified location

            Parameter:
                location (Location): Location to find free locations around

            Result:
                List[Location]: List of Free Available Locations
        """

        free_spots: List[Location] = []

        normal_offsets = self.__retrieveOffset.apply_rules_vision(0)

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

    def find_survivor_bot(self, location: Location):
        """
            Function responsible for finding Survivor Bot's around specified location

            Parameter:
                  location (Location): Location to check for Survivor bot's around

            Result:
                List[Location]: List of Survivor Bot Locations
        """

        # Lazy Loading SurvivorBot Class to prevent Circular Issue
        from model.agents.survivor_bot import SurvivorBot

        survivor_bots: List[Location] = []

        normal_offsets = self.__retrieveOffset.apply_rules_vision(150)

        # For Loop to check for Free Space
        for offset_x, offset_y in normal_offsets:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = (location.get_x() + offset_x) % self.__width
            new_offset_y = (location.get_y() + offset_y) % self.__height

            if isinstance(self.__environment[new_offset_y][new_offset_x], SurvivorBot):
                survivor_bots.append(Location(new_offset_y, new_offset_x))

        return survivor_bots

    def find_spare_part(self, location: Location) -> List[Location]:
        """
        Function Responsible for finding Spare Parts from specified location

            Parameter:
                location (Location): Location to check for spare parts around

            Result:
                List[Location]: List of Spare Parts Locations
        """

        spare_parts: List[Location] = []

        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
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
        """
        Function Responsible for finding the next best move to the recharge station

            Parameter:
                current_location (Location): Location to find the best move to the recharge station
                recharge_location (Location): Recharge station the find next best move for

            Result:
                Location: Location of the next best move
        """

        next_move_x = None
        next_move_y = None

        if current_location.get_x() > recharge_location.get_x():
            next_move_x = current_location.get_x() - 1

        if current_location.get_x() < recharge_location.get_x():
            next_move_x = current_location.get_x() + 1

        else:
            next_move_x = current_location.get_x()

        if current_location.get_y() > recharge_location.get_y():
            next_move_y = current_location.get_y() - 1

        if current_location.get_y() < recharge_location.get_y():
            next_move_y = current_location.get_y() + 1

        else:
            next_move_y = current_location.get_y()

        return Location(next_move_y, next_move_x)

    # TODO: Fix: MalfunctioningDrone is not undefined
    def find_danger_nearby(self, location: Location) -> List[Location]:
        """
        Function Responsible for finding Dangerous Agents nearby

            Parameter:
                location (Location): Location to check for dangerous agents

            Result:
                List[Location]: List of dangerous agents Locations
        """

        danger_nearby: List[Location] = []
        normal_offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
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

        return danger_nearby

    # Display Environment
    def display_environment(self):
        """
        Function Responsible for displaying the current state of the environment

            Parameter:
                None

            Return:
                Multi-Line Grid: Current State of the environment
        """
        for row in range(self.__height):
            print(self.__environment[row])

    def check_space_if_None(self, location: Location) -> bool:
        """
        Function Responsible for checking if the specified space contains nothing in it

            Parameter:
                location (Location): Location to check for empty space

            Return:
               boolean: True if space is empty, otherwise False
        """
        if self.__environment[location.get_y()][location.get_x()] is None:
            return True
        else:
            return False

    def add_objects_to_map(self, list_Location: List[Location], object_toAdd: object):
        """
        Function Responsible for adding multiple objects to multiple locations

            Parameter:
                list_location (List[Location]): List of Locations to add objects to
                objects_toAdd (object): Object to add to the Locations

            Return:
                None
        """

        for location in list_Location:
            self.__environment[location.get_y()][location.get_x()] = object_toAdd

    def add_object(self, location: Location, objectAdd: object):
        self.__environment[location.get_y()][location.get_x()] = objectAdd


    def check_if_agent_is_next_to_another_agent(self, agent1: Agent, agent2: Agent):
        """
        Function Responsible for checking if agent2 is next cell to agent1
        :param agent1:
        :param agent2:
        :return:
        """

        offset = self.__retrieveOffset.apply_rules_vision(0)

        for offset_x, offset_y in offset:

            # Getting coordinates that reflect the position of the Agent
            # E.g coordinates that are around the current Agent position
            new_offset_x = (agent1.get_location().get_x() + offset_x) % self.__width
            new_offset_y = (agent1.get_location().get_y() + offset_y) % self.__height

            # Checking if there is something at those new coordinates
            if self.__environment[new_offset_y][new_offset_x] is agent2:
                return True

            return False