from abc import abstractmethod, ABC
from model.location import Location
from model.agent import Agent
from typing import Optional


class Environment(ABC):
    def __init__(self, width: int, height: int) -> None:
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