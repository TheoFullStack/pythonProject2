from collections import Counter
prompt = None
money = 0
inserted_money = 0
enough_money = False
do_not_stop = True
enough_resources = True
resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

espresso = {
    "Water": 50,
    "Milk": 0,
    "Coffee": 18,
    "Money": 0
}

latte = {
    "Water": 200,
    "Milk": 150,
    "Coffee": 24,
    "Money": 0
}

cappuccino = {
    "Water": 250,
    "Milk": 100,
    "Coffee": 24,
    "Money": 0
}


def money_counter():
    global prompt, money, inserted_money, resources, enough_money,enough_resources
    if prompt == "espresso":
        inserted_money = float(input("Please insert Money for your selected coffee:     "))
        if inserted_money > 1.50 and enough_resources:
            change = inserted_money - 1.50
            money += 1.50
            enough_money = True
            print(f'Here is your change, {change}. Enjoy your Espresso!')
        elif inserted_money == 1.50 and enough_resources:
            money += 1.50
            enough_money = True
            print(f'Here is your espresso. Thank You!')
        elif inserted_money < 1.50:
            print(f'Not enough money bitch. Espresso is 1.50$. You inserted {inserted_money}.')
        else:
            print("Invalid Entry. Try Again.")
    elif prompt == "latte":
        inserted_money = float(input("Please insert Money for your selected coffee:     "))
        if inserted_money > 2.50 and enough_resources:
            change = inserted_money - 2.50
            money += 2.50
            enough_money = True
            print(f'Here is your change, {change}. Enjoy your latte!')
        elif inserted_money == 2.50:
            if enough_resources:
                money += 2.50
                enough_money = True
                print(f'Here is your latte. Thank You!')
        elif inserted_money < 2.50:
            print(f'Not enough money bitch. Latte is 2.50$. You inserted {inserted_money}.')
        else:
            print("Invalid Entry. Try Again.")

    elif prompt == "cappuccino":
        inserted_money = float(input("Please insert Money for your selected coffee:     "))
        if inserted_money > 3.00 and enough_resources:
            change = inserted_money - 3.00
            money += 3.00
            enough_money = True
            print(f'Here is your change, {change}. Enjour your cappuccino!')
        elif inserted_money == 3.00 and enough_resources:
            money += 3.00
            enough_money = True
            print(f'Here is your cappuccino. Thank You!')
        elif inserted_money < 3.00:
            print(f'Not enough money bitch. Cappuccino is 3.00$. You inserted {inserted_money}.')
        else:
            print("Invalid Entry. Try Again.")

    resources["Money"] = float(money)


def substracter() :
    global enough_resources, do_not_stop, money
    global prompt
    global resources
    global latte
    global espresso
    global cappuccino
    if prompt == "latte":
            # Check if you have enough of each ingredient for the latte
            for ingredient, required_quantity in latte.items():
                if ingredient in resources and resources[ingredient] < required_quantity:
                    enough_resources = False
                    print(f"Not enough {ingredient} for a latte.")
            if enough_resources:
                money_counter()
                print("You have enough resources for a latte.")
                temp1 = Counter(resources)
                temp2 = Counter(latte)
                diff = temp1 - temp2
                resources = dict(diff)
            """else:
                print("You do not have enough resources for a latte. Your money is refunded")
                money -= 2.50
                resources["Money"] = float(money)"""

    elif prompt == "espresso":
        for ingredient, required_quantity in espresso.items():
            if ingredient in resources and resources[ingredient] < required_quantity:
                enough_resources = False
                print(f"Not enough {ingredient} for an espresso.")
        if enough_resources:
            money_counter()
            print("You have enough resources for an espresso.")
            temp1 = Counter(resources)
            temp2 = Counter(espresso)
            diff = temp1 - temp2
            resources = dict(diff)
        """else:
            print("You do not have enough resources for an espresso. Your money is refunded")
            money -= 1.50
            resources["Money"] = float(money)"""

    elif prompt == "cappuccino":
        for ingredient, required_quantity in cappuccino.items():
            if ingredient in resources and resources[ingredient] < required_quantity:
                enough_resources = False
                print(f"Not enough {ingredient} for a cappuccino.")
        if enough_resources:
            money_counter()
            print("You have enough resources for an cappuccino.")
            temp1 = Counter(resources)
            temp2 = Counter(cappuccino)
            diff = temp1 - temp2
            resources = dict(diff)
        """else:
            print("You do not have enough resources for a cappuccino. Your money is refunded")
            money -= 3.00
            resources["Money"] = float(money)"""

    if prompt == "off":
        do_not_stop = False
    if prompt == "resources":
        print(resources)






while do_not_stop:
    prompt = str(input("What would you like to drink? espresso/latte/capppucino:    ")).lower()
    substracter()

