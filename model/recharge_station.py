from __future__ import annotations

import random
from typing import TYPE_CHECKING, List

from controller.Config import Config

if TYPE_CHECKING:
    from model.agents.spare_part import SparePart
    from model.location import Location
    from model.agents.survivor_bot import SurvivorBot



class RechargeStation:
    def __init__(self, location: Location) -> None:
        self.__location = location

        self.__spare_part = []

        self.__survivor_bot = []

    def get_location(self) -> Location:
        return self.__location

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

    def bot_creating_chance(self):
        from model.agents.survivor_bot import SurvivorBot
        survivorBotGatherer = False
        survivorBotRepair = False
        for survivorBot in self.__survivor_bot:
            if survivorBotGatherer is False or survivorBotRepair is False:
                if survivorBot.get_bot_type() == "GATHERER":
                    survivorBotGatherer = True

                if survivorBot.get_bot_type() == "REPAIR":
                    survivorBotRepair = True

            else:
                break


        if survivorBotGatherer is True and survivorBotRepair is True:
            randomValue = random.random()

            if randomValue <= Config.PROBABILITY_NEW_GATHERER_BOT:
                newSurvivorBot = SurvivorBot(self.get_location(), "GATHERER")
                newSurvivorBot.set_primary_recharge_station(self)
                return newSurvivorBot

            elif randomValue < Config.PROBABILITY_NEW_REPAIR_BOT:
                newSurvivorBot = SurvivorBot(self.get_location(), "REPAIR")
                newSurvivorBot.set_primary_recharge_station(self)
                return newSurvivorBot

            else:
                return None