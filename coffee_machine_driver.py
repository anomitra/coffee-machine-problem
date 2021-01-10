import json
import os
import sys

from coffee_machine import CoffeeMachine

DEFAULT_TEST_FILE = 'default_test_data.json'
TEST_CASES_FOLDER = 'test_cases'
class CoffeeMachineDriver:

    def __init__(self, test_file):
        with open(test_file, 'r') as file:
            self.test_data = json.load(file).get("machine")

    def run_coffee_machine(self):
        outlets = self.test_data.get("outlets").get("count_n")
        ingredient_data = self.test_data.get("total_items_quantity")
        coffee_machine = CoffeeMachine(outlets)
        coffee_machine.set_ingredients(ingredient_data)
        beverages = self.test_data.get("beverages")
        for beverage_name, beverage_details in beverages.items():
            coffee_machine.dispense_beverage(beverage_name, beverage_details)


if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TEST_FILE
    os.chdir(TEST_CASES_FOLDER)
    path = os.path.abspath(file_name)
    CoffeeMachineDriver(file_name).run_coffee_machine()