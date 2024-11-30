import unittest

import random

from model.agent import Agent
from model.city import City
from model.location import Location


class TestCity(unittest.TestCase):

    def test_width(self):
        city = City(20, 30)
        self.assertEqual(city.get_width(), 20, "Width of the City has not been set properly")  # add assertion here

    def test_height(self):
        city = City(20, 30)

        self.assertEqual(city.get_height(), 30, "Height of the City has not been set properly")  # add assertion here


    def test_get_agent_none(self):
        city = City(width = 20, height = 20)

        self.assertEqual(city.check_space_if_None(Location(5, 5)), True, f"The Space isn't Empty")


    def test_get_agent_agent(self):
        agent = Agent(Location(5,5))
        city = City(width = 20, height = 20)
        city.set_agent(agent, agent.get_location())
        self.assertEqual(city.check_space_if_None(Location(5, 5)), False, f"The agent hasn't been placed properly")
