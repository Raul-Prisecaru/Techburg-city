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



    def run(self):

        # Creating and displaying City Environment
        city_environment = City(self.__width, self.__height)

        while True:
            print("---")
            city_environment.display_environment()
            time.sleep(5)






# Running the Simulation
Simulation(30, 30).run()

