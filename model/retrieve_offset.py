from typing import Tuple, List


class RetrieveOffset:
    def __init__(self):
        self.__rules = []



    def add_rule(self, condition: int, result: List[Tuple[int, int]]):
        self.__rules.append((condition, result))



    def retrieve_offset(self, percentageValue: int):
        for condition, result in self.__rules:
            if condition(percentageValue):
                return result

