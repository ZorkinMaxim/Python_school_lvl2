names = ("Espresso", "Cappuccino", "Robusta")
ingr_1 = {"water": "100ml", "coffee": "10g"}
ingr_2 = {"water": "50ml", "coffee": "10g", "milk": "50ml"}
ingr_3 = {"water": "50ml", "coffee": "10g", "milk": "50ml", "ice": "3 blocks"}

class CoffeeMachine:
    def __init__(self, brand="Philips"):
        self.brand = brand

    def __str__(self):
        return f"The name of Coffee Machine is {self.brand}"

    def makeCoffee(self, name, ingredients):
        if name in names:
            return _CoffeeDrink(name, ingredients)
        else:
            raise TypeError(f"This machine can make only {names} types of Coffee")


class _CoffeeDrink:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"Your drink is {self.name}, contains of {self.ingredients}"



        # if self.ingredients == ingr_1:
        #     return f"Your drink is {names[0]}, contains of {ingr_1}"
        # elif self.ingredients == ingr_2:
        #     return f"Your drink is {names[1]}, contains of {ingr_2}"
        # elif self.ingredients == ingr_3:
        #     return f"Your drink is {names[2]}, contains of {ingr_3}"
        # else:
        #     return "Please repeat!"