from model.agent import Agent
from model.location import Location
from model.city import City

class SparePart(Agent):

    def __init__(self, location: Location):
        super().__init__(location)

    # For Set Location:: IDEA
    #     Check if the position matches with one of the
    #     Recharge Stations and display that
    # E.g Location: Recharge Station 1 // coords: (x : y)


    def act(self, city: City):
        pass

    # Scatter between coordinates 10 - 20
    def __randomly_scatter(self, city: City):
        pass