from model.city import City
from model.location import  Location
from model.agents.survivor_bot import SurvivorBot


class Simulation:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def run(self):
        city_environment = City(self.__width, self.__height)
        city_environment.display_environment()
        bot = SurvivorBot(Location(int(self.__width / 2), int(self.__height / 2)))

        city_environment.set_agent(bot, bot.get_location())
        city_environment.display_environment()


Simulation(10, 10).run()

