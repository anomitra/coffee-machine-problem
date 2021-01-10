import json

from coffee_machine import CoffeeMachine

class CoffeeMachineDriver:

    def __init__(self, test_file='test_data.json'):
        with open(test_file, mode='r') as file:
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
    CoffeeMachineDriver().run_coffee_machine()