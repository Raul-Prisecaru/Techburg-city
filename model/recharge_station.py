from __future__ import annotations

from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from model.agents.spare_part import SparePart
    from model.location import Location
    from model.agents.survivor_bot import SurvivorBot



class RechargeStation:
    def __init__(self):
        self.__station_location = []
        self.__spare_part = []

        self.__survivor_bot = []

    def add_location(self, location: Location) -> None:
        self.__station_location.append(location)


    def return_location(self) -> List[Location]:
        return self.__station_location


    def add_spare_part(self, sparePart: SparePart) -> None:
        self.__spare_part.append(sparePart)

    def get_spare_part(self):
        return self.__spare_part

    def remove_spare_part(self) -> None:
        self.__spare_part.pop()

    def add_survivor_bot(self, survivor_bot: SurvivorBot) -> None:
        self.__survivor_bot.append(survivor_bot)

    def remove_survivor_bot(self) -> None:
        pass



