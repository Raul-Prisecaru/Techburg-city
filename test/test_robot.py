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

    def test_pickUp_spare_part(self):
        city = City(10, 10)
        spare_part_place = Location(5, 6)
        sparePart = SparePart(spare_part_place)

        city.set_agent(sparePart, sparePart.get_location())
        start_location = Location(5,5)
        survivor_bot = SurvivorBot(start_location)
        survivor_bot.act(city)

        # Checking if bot went to the Items Location
        self.assertEqual(survivor_bot.get_location(), spare_part_place, "Survivor bot did not go to the Spare Part Location to pick it up")




