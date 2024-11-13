from __future__ import annotations

from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from model.location import Location



class RechargeStation:
    def __init__(self):
        self.__station_location = []


    def add_location(self, location: Location) -> None:
        self.__station_location.append(location)


    def return_location(self) -> List[Location]:
        return self.__station_location