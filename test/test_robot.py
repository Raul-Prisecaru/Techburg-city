import unittest
from model.agents.survivor_bot import SurvivorBot
from model.location import Location
from model.city import City
from model.agents.spare_part import SparePart


class TestRobotAgent(unittest.TestCase):
    def test_movement(self):
        city = City(10, 10)
        start_location = Location(5,5)
        survivor_bot = SurvivorBot(start_location)
        survivor_bot.act(city)

        self.assertNotEqual(Location(5, 5), survivor_bot.get_location(), "Survivor Bot did not move")



