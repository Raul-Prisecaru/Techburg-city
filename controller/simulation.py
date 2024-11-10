from model.city import City
from model.location import  Location
from model.agents.survivor_bot import SurvivorBot
from model.agents.malfunctioning_drone import MalfunctioningDrone
from model.agents.spare_part import SparePart
import time


class Simulation:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    def run(self):
        # Creating and displaying City Environment
        city_environment = City(self.__width, self.__height)
        # city_environment.display_environment()
        # print("----")

        sparepart = SparePart(Location(0,0))

        sparepart.act(city_environment, 10)
        # city_environment.display_environment()



        # Creating SurvivorBot Agent and setting a location as start
        survivor_bot1 = SurvivorBot(Location(15, 15))
        survivor_bot2 = SurvivorBot(Location(14, 14))
        survivor_bot3 = SurvivorBot(Location(13, 13))
        survivor_bot4 = SurvivorBot(Location(12, 12))

        # Creating Malfunctioning Drone Agent and setting a location as start
        malfunctioning_drone1 = MalfunctioningDrone(Location(1, 1))
        malfunctioning_drone2 = MalfunctioningDrone(Location(2, 2))
        malfunctioning_drone3 = MalfunctioningDrone(Location(3, 3))
        malfunctioning_drone4 = MalfunctioningDrone(Location(4, 4))



        # Placing Agent in the Agents' set location
        city_environment.set_agent(survivor_bot1, survivor_bot1.get_location())
        # city_environment.set_agent(survivor_bot2, survivor_bot2.get_location())
        # city_environment.set_agent(survivor_bot3, survivor_bot3.get_location())
        # city_environment.set_agent(survivor_bot4, survivor_bot4.get_location())
        #
        # city_environment.set_agent(malfunctioning_drone1, malfunctioning_drone1.get_location())
        # city_environment.set_agent(malfunctioning_drone2, malfunctioning_drone2.get_location())
        # city_environment.set_agent(malfunctioning_drone3, malfunctioning_drone3.get_location())
        # city_environment.set_agent(malfunctioning_drone4, malfunctioning_drone4.get_location())

        while True:
            survivor_bot1.act(city_environment)
            # survivor_bot2.act(city_environment)
            # survivor_bot3.act(city_environment)
            # survivor_bot4.act(city_environment)
            #
            # malfunctioning_drone1.act(city_environment)
            # malfunctioning_drone2.act(city_environment)
            # malfunctioning_drone3.act(city_environment)
            # malfunctioning_drone4.act(city_environment)
            print("---")
            city_environment.display_environment()
            time.sleep(10)






# Running the Simulation
Simulation(30, 30).run()

