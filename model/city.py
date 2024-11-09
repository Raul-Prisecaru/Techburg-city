from abc import ABC

from environment import Environment
from location import Location
from agent import Agent
from typing import override, Optional


class City(Environment, ABC):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self.__environment = []

        for _ in range(height):
            self.__environment.append([None] * width)

    def get_agent(self, location: Location) -> Optional[Agent]:
        pass
    def set_agent(self, agent: Agent, location: Location) -> None:
        pass



    