from model.city import City
from model.location import  Location
from model.agents.survivor_bot import SurvivorBot
from model.agents.malfunctioning_drone import MalfunctioningDrone
from model.agents.spare_part import SparePart
from model.recharge_station import RechargeStation
import time


class Simulation:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__rechargeStation = RechargeStation()
        self.__sparePart = SparePart(Location(15, 27))
        self.__survivorBot = SurvivorBot(Location(15, 28))

    def recharge_station_config(self):
        """
        Function responsible for configuring recharge Stations Settings
            Parameter:
                None

            Return:
                None
        """
        self.__rechargeStation.set_location(Location(15,29))
        pass

    def survivor_bots_config(self):
        """
        Function responsible for configuring Survivor Bots
            Parameter:
                None

            Return:
                None
        """
        self.__survivorBot.set_primary_recharge_station(self.__rechargeStation)


    def malfunctioning_drones_config(self):
        """
        Function responsible for configuring Malfunctioning Drones
            Parameter:
                None

            Return:
                None
        """
        pass

    def scavenger_swarms_config(self):
        """
        Function responsible for configuring Scavenger Swarms
            Parameter:
                None

            Return:
                None
        """
        pass

    def spare_parts_config(self):
        """
        Function responsible for configuring Spare Parts
            Parameter:
                None

            Return:
                None
        """
        pass

    def run(self):

        # Creating
        city_environment = City(self.__width, self.__height)

        # Adding To the environment
        city_environment.set_agent(self.__rechargeStation, self.__rechargeStation.get_location())
        city_environment.set_agent(self.__sparePart, self.__sparePart.get_location())
        city_environment.set_agent(self.__survivorBot, self.__survivorBot.get_location())


        while True:
            print("---")
            city_environment.display_environment()
            self.__survivorBot.act(city_environment)
            time.sleep(2)






# Running the Simulation
Simulation(30, 30).run()

