import os

from abc import ABC
from model.city import City
from model.agent import Agent
from model.location import Location
current_dir = os.path.dirname(__file__)
move_up_dir = os.path.dirname(current_dir)


class SurvivorBot(Agent):
    def __init__(self, location: Location):
        super().__init__(location)


    def act(self, city: City):
        pass

    def __move(self, city: City):
        pass



