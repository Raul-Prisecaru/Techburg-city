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
        self.__rechargeStation.set_location(Location(15,29))
        self.__sparePart = SparePart(Location(15, 27))
        self.__survivorBot = SurvivorBot(Location(15, 28))

    def run(self):

        # Creating and displaying City Environment
        city_environment = City(self.__width, self.__height)
        city_environment.set_agent(self.__rechargeStation, self.__rechargeStation.get_location())
        city_environment.set_agent(self.__sparePart, self.__sparePart.get_location())
        city_environment.set_agent(self.__survivorBot, self.__survivorBot.get_location())


        while True:
            print("---")
            city_environment.display_environment()
            self.__survivorBot.act(city_environment, self.__rechargeStation)
            time.sleep(2)






# Running the Simulation
Simulation(30, 30).run()

