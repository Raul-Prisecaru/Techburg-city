import time
import unittest
from unittest import SkipTest, skipIf

from model.agents.survivor_bot import SurvivorBot
from model.location import Location
from model.city import City
from model.agents.spare_part import SparePart
from model.recharge_station import RechargeStation


class TestRobotAgent(unittest.TestCase):

    def test_movement(self):
        """
        Simple Test to verify survivor bot can move to a free location
        """
        self.__recharge_Station = RechargeStation()
        self.__recharge_Station.set_location(Location(5, 9))
        city = City(10, 10)
        start_location = Location(5,5)
        survivor_bot = SurvivorBot(start_location)

        survivor_bot.set_primary_recharge_station(self.__recharge_Station)


        survivor_bot.act(city)

        self.assertNotEqual(Location(5, 5), survivor_bot.get_location(), "Survivor Bot did not move")

    def test_pickUp_spare_part(self):
        """
        Simple Test to verify survivor bot can pick up a spare part
        """
        self.__recharge_Station = RechargeStation()
        self.__recharge_Station.set_location(Location(5, 9))

        city = City(20, 20)
        survivor_bot = SurvivorBot(Location(5,5))
        survivor_bot.set_primary_recharge_station(self.__recharge_Station)

        spare_part = SparePart(Location(5,4))

        city.set_agent(survivor_bot, survivor_bot.get_location())

        city.set_agent(spare_part, spare_part.get_location())

        while len(survivor_bot.get_inventory()) != 1:
            survivor_bot.act(city)


        self.assertEqual(survivor_bot.get_location().get_x(), spare_part.get_location().get_x(), "Survivor bot did not go to the Spare Part X Location")
        self.assertEqual(survivor_bot.get_location().get_y(), spare_part.get_location().get_y(), "Survivor bot did not go to the Spare Part Y Location")

        inventory = survivor_bot.get_inventory()
        self.assertIn(spare_part, inventory, "spare part was not corrected added to the inventory")

    def test_travel_to_recharge_station(self):
        """
        Simple test to verify survivor bot can travel to a recharge station and store it's spare part to the recharge station
        """
        self.__recharge_Station = RechargeStation()
        self.__recharge_Station.set_location(Location(5, 9))

        city = City(10, 10)
        survivor_bot = SurvivorBot(Location(5,8))
        survivor_bot.set_primary_recharge_station(self.__recharge_Station)


        spare_part = SparePart(Location(5,7))

        city.set_agent(survivor_bot, survivor_bot.get_location())

        city.set_agent(spare_part, spare_part.get_location())
        city.set_agent(self.__recharge_Station, self.__recharge_Station.get_location())

        while len(self.__recharge_Station.get_survivor_bot()) != 1:
            survivor_bot.act(city)



        # TODO: Later to be improved to a isInstance assert Check
        self.assertEqual(1, len(self.__recharge_Station.get_survivor_bot()), "Survivor bot did not insert into the recharge Station" )
        self.assertEqual(1, len(self.__recharge_Station.get_spare_part()), "Survivor bot did not insert the spare part into the recharge Station inventory" )



    def test_survivor_bot_energy(self):
        """
        Simple Test to verify survivor bot can and cannot move dependent on energy levels
        """
        self.__recharge_Station = RechargeStation()
        self.__recharge_Station.set_location(Location(5, 9))

        city = City(20, 20)
        start_location = Location(5, 8)
        survivor_bot = SurvivorBot(start_location)
        survivor_bot.set_primary_recharge_station(self.__recharge_Station)

        city.set_agent(survivor_bot, survivor_bot.get_location())
        city.set_agent(self.__recharge_Station, self.__recharge_Station.get_location())

        survivor_bot.set_energy(0)
        movements = []

        for _ in range(3):
            survivor_bot.act(city)
            movements.append(survivor_bot.get_location())

        self.assertEqual(start_location, movements[0], "Survivor Bot Moved during it's first turn of no energy")
        self.assertEqual(start_location, movements[1], "Survivor Bot Moved during it's second turn of no energy")
        self.assertEqual(start_location, movements[2], "Survivor Bot Moved during it's third turn of no energy")

    def test_survivor_bot_death(self):
        """
        Simple test to verify survivor bot disappears from grid after a few turns of no energy
        """
        self.__recharge_Station = RechargeStation()
        self.__recharge_Station.set_location(Location(5, 9))

        city = City(10, 10)
        start_location = Location(5, 8)
        survivor_bot = SurvivorBot(start_location)
        survivor_bot.set_primary_recharge_station(self.__recharge_Station)


        city.set_agent(survivor_bot, survivor_bot.get_location())

        city.set_agent(self.__recharge_Station, self.__recharge_Station.get_location())

        survivor_bot.set_energy(0)
        movements = []

        for _ in range(5):
            survivor_bot.act(city)
            movements.append(survivor_bot.get_location())

        print(survivor_bot.get_energy_turn())
        self.assertEqual(start_location, movements[0], "Survivor Bot Moved during it's first turn of no energy")
        self.assertEqual(start_location, movements[1], "Survivor Bot Moved during it's second turn of no energy")
        self.assertEqual(start_location, movements[2], "Survivor Bot Moved during it's third turn of no energy")
        self.assertEqual(start_location, movements[3], "Survivor Bot Moved during it's fourth turn of no energy")
        self.assertEqual(start_location, movements[4], "Survivor Bot Moved during it's fifth turn of no energy")
        self.assertEqual(city.check_space_if_None(start_location), True, "Survivor Bot has not been removed from the grid")

    def test_survivor_bot_consume_spare_part(self):
        """
        Simple test to verify survivor bot disappears from grid after a few turns of no energy
        """
        self.__recharge_Station = RechargeStation()
        self.__recharge_Station.set_location(Location(5, 9))

        city = City(10, 10)
        start_location = Location(5, 8)
        survivor_bot = SurvivorBot(start_location)
        survivor_bot.set_primary_recharge_station(self.__recharge_Station)

        spare_part = SparePart(Location(5,7))

        city.set_agent(survivor_bot, survivor_bot.get_location())
        city.set_agent(spare_part, spare_part.get_location())

        survivor_bot.set_energy(5)

        while survivor_bot.get_energy() <= 5:
            survivor_bot.act(city)



        # TODO: Ensure to test that the spare part is also removed from inventory because consumed
        self.assertGreater(survivor_bot.get_energy(), 0, "Energy has not increased after consuming part")
        self.assertEqual(len(survivor_bot.get_inventory()), 0, "Spare Part has not been properly removed from inventory")

    # def test_survivor_bot_not_enough_energy_travel_back(self):
    #     """
    #     Simple test to verify the responsible function returns true or false dependent if survivor bot has enough energy to travel back
    #     """
    #     pass