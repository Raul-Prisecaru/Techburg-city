from typing import Tuple, List


class RetrieveOffset:
    def __init__(self):
        self.__rules = {}



    def add_rule_for_speed_enhancement(self, condition: int, result: List[Tuple[int, int]]):
        if "speed" not in self.__rules:
            self.__rules["speed"] = []

        self.__rules["speed"].append((condition, result))

    def add_rule_for_vision_enhancement(self, condition: int, result: List[Tuple[int, int]]):
        if "vision" not in self.__rules:
            self.__rules["vision"] = []

        self.__rules["vision"].append((condition, result))

    def add_rule_for_energy_enhancement(self, condition: int, result: List[Tuple[int, int]]):
        if "energy" not in self.__rules:
            self.__rules["energy"] = []

        self.__rules["energy"].append((condition, result))

    def apply_rules_vision(self, percentageValue: int):
        for condition, result in self.__rules["vision"]:
                if condition(percentageValue):
                    return result


    def display_rules(self):
        for key, pair in self.__rules.items():
            print(f"Rule Category: {key}")
            for condition, result in pair:
                print("Condition:", condition)
                print("Result:", result)

