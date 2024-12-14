from typing import List

from controller.Config import Config
from model.agents.scavenger_swarm import ScavengerSwarm
from model.city import City
from model.location import  Location
from model.agents.survivor_bot import SurvivorBot
from model.agents.malfunctioning_drone import MalfunctioningDrone
from model.agents.spare_part import SparePart
from model.recharge_station import RechargeStation
from view.Gui import Gui
import time


class Simulation:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

        self.__is_running = False

        self.__city_environment = City(self.__width, self.__height)
        self.__sparePart = SparePart(self.__city_environment)
        self.__survivorBots = []
        self.__MalfunctioningDrones = []
        self.__ScavengerSwarms = []
        self.__rechargeStation = []

        # self.__agent_colours = {self.__survivorBots: Config.SURVIVOR_BOT_COLOUR, self.__MalfunctioningDrones: Config.MALFUNCTIONING_DRONE_COLOUR, self.__ScavengerSwarms: Config.SCAVENGER_SWARM_COLOUR}
        self.__agent_colours = {
            SurvivorBot: Config.SURVIVOR_BOT_COLOUR,
            MalfunctioningDrone: Config.MALFUNCTIONING_DRONE_COLOUR,
            ScavengerSwarm: Config.SCAVENGER_SWARM_COLOUR,
            RechargeStation: Config.RECHARGE_STATION_COLOUR,
            SparePart: Config.SPARE_PART_COLOUR}

        self.__gui = Gui(self.__city_environment, self.__agent_colours)
        self.__gui.render()

    def create_recharge_station(self, total: int) -> List[RechargeStation]:
        """
        Function responsible for creating Recharge Station for the environment
            Parameter:
                total (int): Number of Recharge Station to be created

            Return:
                 List[RechargeStation]: List containing specified number of Recharge Stations

        """

        for number in range(total):
            self.__rechargeStation.append(RechargeStation(Location((15 - number), 29)))

        return self.__rechargeStation


    def recharge_station_config(self):
        """
        Function responsible for configuring recharge Stations Settings
            Parameter:
                None

            Return:
                None
        """

        pass


    def recharge_station_add_environment(self):
        """
        Function responsible for adding the Recharge Stations to the environment
        """
        for rechargeStation in self.__rechargeStation:
            self.__city_environment.add_object(rechargeStation.get_location(), rechargeStation)


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

    def scatter_spare_parts(self, total: int, start_location: int, end_location: int):
        """
        Function responsible for creating and scattering Spare Parts across the environment
            Parameter:
                Total (int): Total Numbers of Spare Parts to scatter
                startLocation (int): Minimum width to add Spare Parts to
                endLocation (int): Maximum width to add Spare Parts to

            Return:
                None
        """

        self.__sparePart.randomly_scatter(total, start_location, end_location)

    def __update(self):

        self.survivor_bots_execute()
        # for survivorBot in self.__survivorBots:
        #     survivorBot.act(self.__city_environment)

    def __render(self):
        self.__gui.render()

    def run(self):

        self.__is_running = True

        # Creating
        self.create_survivor_bots(5)
        self.create_recharge_station(1)

        # Configs
        self.survivor_bots_config()
        self.recharge_station_config()

        # Adding
        self.survivor_bots_add_environment()
        self.recharge_station_add_environment()
        self.scatter_spare_parts(10, 5, 20)

        self.__city_environment.display_environment()

        while self.__is_running:
            self.__update()
            self.__render()
            time.sleep(1)
            if self.__gui.is_closed():
                self.__is_running = False





            # print("---")
            # # self.__city_environment.display_environment()
            # self.survivor_bots_execute()
            # self.__city_environment.display_environment()
            # time.sleep(1)



# Running the Simulation
Simulation(30, 30).run()

