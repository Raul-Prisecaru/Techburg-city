import random
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
    def __init__(self) -> None:
        self.__width = Config.GRID_WIDTH
        self.__height = Config.GRID_HEIGHT

        self.__is_running = False

        self.__city_environment = City(self.__width, self.__height)

        # self.__agent_colours = {self.__survivorBots: Config.SURVIVOR_BOT_COLOUR, self.__MalfunctioningDrones: Config.MALFUNCTIONING_DRONE_COLOUR, self.__ScavengerSwarms: Config.SCAVENGER_SWARM_COLOUR}
        self.__agent_colours = {
            SurvivorBot: Config.SURVIVOR_BOT_COLOUR,
            MalfunctioningDrone: Config.MALFUNCTIONING_DRONE_COLOUR,
            ScavengerSwarm: Config.SCAVENGER_SWARM_COLOUR,
            RechargeStation: Config.RECHARGE_STATION_COLOUR,
            SparePart: Config.SPARE_PART_COLOUR}

        self.__gui = Gui(self.__city_environment, self.__agent_colours)
        self.__gui.render()

    def create_recharge_station(self, total: int) -> None:
        """
        Function responsible for creating Recharge Station for the environment
            Parameter:
                total (int): Number of Recharge Station to be created

            Return:
                 List[RechargeStation]: List containing specified number of Recharge Stations

        """

        for number in range(total):
            self.__city_environment.add_recharge_station_to_list(RechargeStation(Location((15 - number), 29)))


    def create_spare_parts(self, total: int):
        random_size = random.choice([3, 5, 7])

        for sparePart in range(total):
            self.__city_environment.add_spare_parts_to_list(SparePart(self.__city_environment, random_size))


    def recharge_station_config(self):
        """
        Function responsible for configuring recharge Stations Settings
            Parameter:
                None

            Return:
                None
        """


        pass


    def spare_part_execute(self):

        for sparePart in self.__city_environment.get_spare_parts_list():
            for rechargeStation in self.__city_environment.get_recharge_station_list():

                if sparePart.get_location() == rechargeStation.get_location():
                    if sparePart.get_enhancementValue() < sparePart.get_size():
                        sparePart.regenerate_enhancementValue()


                elif sparePart.get_location() != rechargeStation.get_location():
                    if sparePart.get_enhancementValue() > 0:
                        sparePart.corrode_enhancementValue()



    def recharge_station_add_environment(self):
        """
        Function responsible for adding the Recharge Stations to the environment
        """
        for rechargeStation in self.__city_environment.get_recharge_station_list():
            self.__city_environment.add_object(rechargeStation.get_location(), rechargeStation)


    def recharge_station_execute(self):

        for rechargeStation in self.__city_environment.get_recharge_station_list():
            survivor_bot_created = rechargeStation.bot_creating_chance()

            if survivor_bot_created is not None:
                self.__city_environment.add_survivor_bot_to_list(survivor_bot_created)


    def create_survivor_bots(self, total: int) -> None:
        """
        Function responsible for creating survivor bots for the environment
            Parameter:
                total (int): Number of Survivor Bots to be created

            Return:
                 List[SurvivorBot]: List containing specified number of Survivor Bots

        """

        for number in range(total):
            self.__city_environment.add_survivor_bot_to_list(SurvivorBot(Location((18 - number), 28), random.choice(["GATHERER", "REPAIR"])))



    def survivor_bots_config(self):

        """
        Function responsible for configuring Survivor Bots
            Parameter:
                None

            Return:
                None
        """
        rechargeStation: RechargeStation = self.__city_environment.get_recharge_station_list()[0]
        for survivorBot in self.__city_environment.get_survivor_bot_list():

            survivorBot.set_primary_recharge_station(rechargeStation)


    def survivor_bots_add_environment(self):
        """
        Function responsible for adding the survivor bots to the Environment

            Parameter:
                None

            Return:
                None

        """
        for survivorBot in self.__city_environment.get_survivor_bot_list():
            self.__city_environment.set_agent(survivorBot, survivorBot.get_location())


    def survivor_bots_execute(self):
        """
        Function responsible for allowing the survivor bot to execute actions

            Parameter:
                None

            Result:
                None
        """

        for survivorBot in self.__city_environment.get_survivor_bot_list():
            survivorBot.act(self.__city_environment)
            print(f"""
            Survivor Bot: {survivorBot}
            Location: {survivorBot.get_location().get_x()}  {survivorBot.get_location().get_y()}
            Type: {survivorBot.get_bot_type()}
            Energy: {survivorBot.get_energy()}
            Priority: {survivorBot.get_priority()}
            Inventory: {survivorBot.get_holding_item()}
            Energy Enhancements: {survivorBot.get_energy_enhancement()}
            Speed Enhancements: {survivorBot.get_speed_enhancement()}
            Vision Enhancements: {survivorBot.get_vision_enhancement()}
""")

    def create_malfunctioning_drones(self, total: int) -> None:
        """
         Function responsible for creating Malfunctioning Drones for the environment
             Parameter:
                 total (int): Number of Malfunctioning Drones to be created

             Return:
                 List[MalfunctioningDrone]: List containing specified number of Malfunctioning Drones
        """
        for number in range(total):
            self.__city_environment.add_malfunctioning_drone_to_list(MalfunctioningDrone(Location(10 - number, 5)))

    def malfunctioning_drones_config(self):
        """
        Function responsible for configuring Malfunctioning Drones
            Parameter:
                None

            Return:
                None
        """
        pass

    def malfunctioning_drones_add_environment(self):
        for malfunctioningDrone in self.__city_environment.get_malfunctioning_drone_list():
            self.__city_environment.set_agent(malfunctioningDrone, malfunctioningDrone.get_location())


    def malfunctioning_drones_execute(self):
        for malfunctioningDrone in self.__city_environment.get_malfunctioning_drone_list():
            malfunctioningDrone.act(self.__city_environment)

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

    def scatter_spare_parts(self, start_location: int, end_location: int):
        """
        Function responsible for creating and scattering Spare Parts across the environment
            Parameter:
                Total (int): Total Numbers of Spare Parts to scatter
                startLocation (int): Minimum width to add Spare Parts to
                endLocation (int): Maximum width to add Spare Parts to

            Return:
                None
        """
        for sparePart in self.__city_environment.get_spare_parts_list():
            sparePart.randomly_scatter(start_location, end_location)

    def __update(self):

        self.survivor_bots_execute()
        # self.malfunctioning_drones_execute()
        self.spare_part_execute()
        self.recharge_station_execute()

    def __render(self):
        self.__gui.render()

    def run(self):

        self.__is_running = True

        # Creating
        self.create_survivor_bots(Config.MAX_SURVIVOR_BOT)
        self.create_malfunctioning_drones(Config.MAX_MALFUNCTIONING_DRONE)
        self.create_recharge_station(1)
        self.create_spare_parts(Config.MAX_SPARE_PARTS)

        # Configs
        self.survivor_bots_config()
        self.recharge_station_config()

        # Adding
        self.survivor_bots_add_environment()
        # self.malfunctioning_drones_add_environment()
        self.recharge_station_add_environment()
        self.scatter_spare_parts(0, 29)

        self.__city_environment.display_environment()

        while self.__is_running:
            self.__update()
            self.__render()
            time.sleep(Config.SIMULATION_TIMER)
            if self.__gui.is_closed():
                self.__is_running = False



# Running the Simulation
Simulation().run()

