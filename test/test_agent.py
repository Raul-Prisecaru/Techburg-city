import unittest
from model.agent import Agent
from model.location import Location

class TestAgent(unittest.TestCase):

    def test_getter(self):
        agent = Agent(Location(1,2))
        self.assertEqual(agent.get_location().get_x(), 1, "Agent's X value hasn't been configured properly")
        self.assertEqual(agent.get_location().get_y(), 2, "Agent's Y value hasn't been configured properly")


    def test_setter(self):
        agent = Agent(Location(1,2))
        agent.set_location(Location(3, 4))

        self.assertEqual(agent.get_location().get_x(), 3, "Agent's X value hasn't been updated properly")
        self.assertEqual(agent.get_location().get_y(), 4, "Agent's Y value hasn't been updated properly")
