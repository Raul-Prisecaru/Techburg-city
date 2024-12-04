from typing import List

from model.agents.scavenger_swarm import ScavengerSwarm
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
        self.__sparePart = []
        self.__survivorBots = []
        self.__MalfunctioningDrones = []
        self.__ScavengerSwarms = []
        self.__rechargeStation = RechargeStation()
        self.__city_environment = City(self.__width, self.__height)


    def recharge_station_config(self):
        """
        Function responsible for configuring recharge Stations Settings
            Parameter:
                None

            Return:
                None
        """
        self.__rechargeStation.set_location(Location(15,29))


    def create_survivor_bots(self, total: int) -> List[SurvivorBot]:
        """
        Function responsible for creating survivor bots for the environment
            Parameter:
                total (int): Number of Survivor Bots to be created

            Return:
                 List[SurvivorBot]: List containing specified number of Survivor Bots

        """

        for number in range(total):
            self.__survivorBots.append(SurvivorBot(Location((15 - number), 28)))

        return self.__survivorBots


    def survivor_bots_config(self):

        """
        Function responsible for configuring Survivor Bots
            Parameter:
                None

            Return:
                None
        """

        for survivorBot in self.__survivorBots:

            survivorBot.set_primary_recharge_station(self.__rechargeStation)


    def survivor_bots_add_environment(self):
        """
        Function responsible for adding the survivor bots to the Environment

            Parameter:
                None

            Return:
                None

        """
        for survivorBot in self.__survivorBots:
            self.__city_environment.set_agent(survivorBot, survivorBot.get_location())


    def survivor_bots_execute(self):
        """
        Function responsible for allowing the survivor bot to execute actions

            Parameter:
                None

            Result:
                None
        """

        for survivorBot in self.__survivorBots:
            survivorBot.act(self.__city_environment)
            print(f"""
            Survivor Bot: {survivorBot}
            X Location: {survivorBot.get_location().get_x()} {survivorBot.get_location().get_y()}
            Y Location: {survivorBot.get_location().get_x()} {survivorBot.get_location().get_y()}""")

    def create_malfunctioning_drones(self, total: int) -> List[MalfunctioningDrone]:
        """
         Function responsible for creating Malfunctioning Drones for the environment
             Parameter:
                 total (int): Number of Malfunctioning Drones to be created

             Return:
                 List[MalfunctioningDrone]: List containing specified number of Malfunctioning Drones
        """
        pass

    def malfunctioning_drones_config(self):
        """
        Function responsible for configuring Malfunctioning Drones
            Parameter:
                None

            Return:
                None
        """
        pass

    def create_scavenger_swarms(self) -> List[ScavengerSwarm]:
        """
         Function responsible for creating Scavenger Swarms for the environment
             Parameter:
                 total (int): Number of Scavenger Swarms to be created

             Return:
                 List[MalfunctioningDrone]: List containing specified number of Scavenger Swarms
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
        self.create_survivor_bots(5)

        # Configs
        self.survivor_bots_config()
        self.recharge_station_config()

        self.__city_environment.display_environment()

        while True:
            print("---")
            # self.__city_environment.display_environment()
            self.survivor_bots_execute()
            self.__city_environment.display_environment()
            time.sleep(1)






# Running the Simulation
Simulation(30, 30).run()

