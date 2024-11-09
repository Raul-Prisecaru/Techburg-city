from abc import abstractmethod, ABC
from location import Location
from agent import Agent
from typing import Optional


class Environment(ABC):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height


    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height

    @abstractmethod
    def get_agent(self, location: Location) -> Optional[Agent]:
        pass
    
    @abstractmethod
    def set_agent(self, agent: Agent, location: Location) -> None:
        pass