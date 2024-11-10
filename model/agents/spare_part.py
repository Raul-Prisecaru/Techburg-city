from random import random, randint

from model.agent import Agent
from model.location import Location
from model.city import City

class SparePart(Agent):

    def __init__(self, location: Location) -> None:
        super().__init__(location)

    # For Set Location:: IDEA
    #     Check if the position matches with one of the
    #     Recharge Stations and display that
    # E.g Location: Recharge Station 1 // coords: (x : y)


    def act(self, city: City, number_spare_parts: int) -> None:
        self.__randomly_scatter(city, number_spare_parts)

    # IDEA:
    # Scatter between coordinates 10 - 20
    # Later to dynamically adapt
    # Get width and height and subtract 10 from each

    def __randomly_scatter(self, city: City, number_spare_parts: int) -> None:
        # List to store locations to plot the Spare Parts
        spare_parts_locations = []

        # While loop to continue generating Locations to store Spare Part until
        # We get the desired amount of locations
        while len(spare_parts_locations) != number_spare_parts:
            # Randomly generate int value for X and Y between 10 and 20
            # Which will be provided to the Location Class
            location = Location(randint(10, 20), randint(10, 20))

            # Checking if there is an empty space at that specific Location
            if city.check_space(location):
                # Looping through the List to see if there is a duplicate
                # Probably worth looking for much efficient route

                for spare_location in spare_parts_locations:

                    # If there's a match, go back to the start of the loop
                    if location == spare_location:
                        continue
                # Once outside the loop, add to the List of valid Locations
                spare_parts_locations.append(location)

            # If there's something there, Generate Another Location
            else:
                continue

        # After Breaking out of the Loop,
        # Call the city function to loop through the list and add to the environment
        city.add_objects_to_map(spare_parts_locations, "Spare_part")






