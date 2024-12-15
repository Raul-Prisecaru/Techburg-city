import unittest

from model.agents.malfunctioning_drone import MalfunctioningDrone
from model.agents.survivor_bot import SurvivorBot
from model.location import Location
from model.city import City
from model.agents.spare_part import SparePart
from model.recharge_station import RechargeStation


class TestDroneAgent(unittest.TestCase):

    def test_movement(self):
        """
        Simple Test to verify Drone can move around the environment
        """
        city = City(10, 10)

        start_location = Location(5,5)

        malfunctioning_drone = MalfunctioningDrone(start_location)

        malfunctioning_drone.act(city)

        self.assertNotEqual(start_location, malfunctioning_drone.get_location(), "Drone did not move")


    def test_hibernation(self):
        """
        Simple Test to verify Drone can hibernate
        """

        city = City(10, 10)

        start_location = Location(5,5)

        malfunctioning_drone = MalfunctioningDrone(start_location)

        malfunctioning_drone.set_energy(0)

        malfunctioning_drone.act(city)

        self.assertGreater(malfunctioning_drone.get_energy(), 0, "Drone's Energy did not increase")
        self.assertEqual(start_location, malfunctioning_drone.get_location(), "Drone moved during hibernation")