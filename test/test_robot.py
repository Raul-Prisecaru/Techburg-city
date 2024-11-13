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
        survivor_bot = SurvivorBot(Location(5,5))

        spare_part = SparePart(Location(5,4))

        city.set_agent(survivor_bot, survivor_bot.get_location())

        city.set_agent(spare_part, spare_part.get_location())

        print(survivor_bot.get_inventory())

        survivor_bot.act(city)

        city.display_environment()


        self.assertEqual(survivor_bot.get_location().get_x(), spare_part.get_location().get_x(), "Survivor bot did not go to the Spare Part X Location")
        self.assertEqual(survivor_bot.get_location().get_y(), spare_part.get_location().get_y(), "Survivor bot did not go to the Spare Part Y Location")

        # bot_inventory = survivor_bot.get_inventory()
        # print(len(bot_inventory))
        #
        # self.assertNotEqual(len(bot_inventory), 0, "Survivor bot did not pick up the Spare Part")


