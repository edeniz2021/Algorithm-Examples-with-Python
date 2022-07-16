MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
   "coffee": 100,
}
ingredent = { }
is_on = True
def check(a):
    for i in a:
        if a[i]> resources[i]:
            print("they dont have enough")
            return False
    return True
def bill():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def succesful(pay,a):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if pay>= a:
        change = round(pay- a, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += a
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make(name,drink):
    for i in drink:
        resources[i]-=drink[i]
    print(f"Here is your {name} ☕️. Enjoy!")
while is_on:
    order = input("What would you like?(espreso/latte/cappuccino) :")
    order = order.lower()
    if order == 'off':
        is_on = False
    elif order == 'report':
        print("\nWater: ",resources['water'],"ml")
        print("Milk: ", resources['milk'],"ml")
        print("Coffee: ", resources['coffee'],"gr")
        print("Money: $",profit)
    else:
        drink=MENU[order]
        if check(drink["ingredients"]):
            buy = bill()
            if succesful(buy,drink["cost"]):
                make(order,drink["ingredients"])


