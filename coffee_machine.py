from collections import defaultdict
from enum import Enum


class Status(Enum):

    NOT_AVAILABLE = "not available"
    NOT_SUFFICIENT = "not sufficient"
    AVAILABLE = "available"


class CoffeeMachine:
    """
    This class represents a coffee machine and all it's functionalities
    """
    def __init__(self, outlets):
        try:
            outlets = float(outlets)
            if not outlets.is_integer():
                raise ValueError
            outlets = int(outlets)
            if outlets < 1:
                raise ValueError
        except ValueError:
            print("Invalid outlet count! Please provide a positive number.")
            exit(0)
        self.outlets = outlets
        self.ingredients = defaultdict()

    def set_ingredients(self, ingredient_data):
        self.ingredients = ingredient_data

    def get_ingredient(self, name):
        return self.ingredients.get(name)

    def _check_ingredient(self, name, quantity):

        available_quantity = self.ingredients.get(name)
        if available_quantity is None:
            return Status.NOT_AVAILABLE
        if available_quantity < quantity:
            return Status.NOT_SUFFICIENT
        return Status.AVAILABLE

    def use_ingredient(self, name, quantity):

        self.ingredients[name] -= quantity
        return quantity

    def refill_ingredient(self, name, quantity):

        available_quantity = self.ingredients.get(name)
        if available_quantity is None:
            return Status.NOT_AVAILABLE

        self.ingredients[name] += quantity

    def dispense_beverage(self, beverage_name, beverage_data):
        """
        Dispensing a beverage as per the given ingredient details. If successful, this function returns `True` and
        otherwise it returns `False`
        :param beverage_name:
        :param beverage_data:
        :return bool:
        """
        for ingredient, quantity in beverage_data.items():
            ingredient_status = self._check_ingredient(ingredient, quantity)
            if ingredient_status != Status.AVAILABLE:
                print("{} cannot be prepared because {} is {}".format(beverage_name, ingredient, ingredient_status.value))
                return False
        for ingredient, quantity in beverage_data.items():
            self.use_ingredient(ingredient, quantity)
        print("{} is prepared".format(beverage_name))
        return True
