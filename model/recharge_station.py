from __future__ import annotations

from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from model.agents.spare_part import SparePart
    from model.location import Location
    from model.agents.survivor_bot import SurvivorBot



class RechargeStation:
    def __init__(self):
        self.__location = Location
        self.__spare_part = []

        self.__survivor_bot = []

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, new_location: Location):
        self.__location = new_location

    def add_spare_part(self, sparePart: SparePart) -> None:
        self.__spare_part.append(sparePart)

    def get_spare_part(self):
        return self.__spare_part

    def remove_spare_part(self) -> None:
        if len(self.__spare_part) != 0:
            self.__spare_part.pop()
        else:
            print("Recharge Stations holds no Survivor Bots")


    def add_survivor_bot(self, survivor_bot: SurvivorBot) -> None:
        self.__survivor_bot.append(survivor_bot)

    def get_survivor_bot(self):
        return self.__survivor_bot

    def remove_survivor_bot(self, survivor_bot: SurvivorBot) -> None:
        if len(self.__survivor_bot) != 0:
            self.__survivor_bot.remove(survivor_bot)

        else:
            print("Recharge Stations holds no Survivor Bots")


