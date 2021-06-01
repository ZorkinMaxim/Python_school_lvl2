from coffee import *

machine = CoffeeMachine()
print(machine)
print("_______________________________________________________________________________________")
drink1 = machine.makeCoffee("Espresso", ingr_1)
drink2 = machine.makeCoffee("Cappuccino", ingr_2)
drink3 = machine.makeCoffee("Robusta", ingr_3)

# drink4 = machine.makeCoffee("Ristr", {"water": "2g"})

print(drink1)
print(drink2)
print(drink3)

# print(drink4)

# coffee_1 = CoffeeMachine()
# coffee_2 = CoffeeMachine.makeCoffee(2, "Cappuccino", ingr_2)
# coffee_3 = CoffeeMachine.makeCoffee(3, "Robusta", ingr_3)

# print(coffee_1)
# print(coffee_2)
# print(coffee_3)