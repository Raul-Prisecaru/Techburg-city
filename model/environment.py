from abc import abstractmethod, ABC
from model.location import Location
from model.agent import Agent
from typing import Optional


class Environment(ABC):
    # Class takes width and height for setting how big the environment grid to be
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    # Returns Width
    def get_width(self) -> int:
        return self.__width

    # Returns Height
    def get_height(self) -> int:
        return self.__height

    # Returns Agent if found at provided location. Returns None otherwise
    @abstractmethod
    def get_agent(self, location: Location) -> Optional[Agent]:
        pass

    # Sets Agent at provided Location
    @abstractmethod
    def set_agent(self, agent: Agent, location: Location) -> None:
        pass