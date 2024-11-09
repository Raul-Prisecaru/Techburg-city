from model.city import City
from model.location import  Location
from model.agents.survivor_bot import SurvivorBot
import time


class Simulation:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    def run(self):
        # Creating and displaying City Environment
        city_environment = City(self.__width, self.__height)
        city_environment.display_environment()
        print("----")


        # Creating SurvivorBot Agent and setting it to center location as start
        survivor_bot1 = SurvivorBot(Location(15, 15))
        survivor_bot2 = SurvivorBot(Location(14, 14))
        survivor_bot3 = SurvivorBot(Location(13, 13))
        survivor_bot4 = SurvivorBot(Location(12, 12))

        # Placing Agent in the Agents' set location
        city_environment.set_agent(survivor_bot1, survivor_bot1.get_location())
        city_environment.set_agent(survivor_bot2, survivor_bot2.get_location())
        city_environment.set_agent(survivor_bot3, survivor_bot3.get_location())
        city_environment.set_agent(survivor_bot4, survivor_bot4.get_location())

        while True:
            survivor_bot1.act(city_environment)
            survivor_bot2.act(city_environment)
            survivor_bot3.act(city_environment)
            survivor_bot4.act(city_environment)
            city_environment.set_agent(survivor_bot1, survivor_bot1.get_location())
            city_environment.set_agent(survivor_bot2, survivor_bot2.get_location())
            city_environment.set_agent(survivor_bot3, survivor_bot3.get_location())
            city_environment.set_agent(survivor_bot4, survivor_bot4.get_location())
            print("---")
            city_environment.display_environment()
            time.sleep(1)






# Running the Simulation
Simulation(20, 20).run()

