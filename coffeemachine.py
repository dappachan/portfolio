menu = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

tot_mon = 0.0
more_resources = True
while more_resources:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        break
    if order == "report":
        for ing in resources:
            if ing == "water" or ing == "milk":
                print(ing.capitalize() + ":  " + str(resources[ing]) + "ml")
            elif ing == "coffee":
                print(ing.capitalize() + ":  " + str(resources[ing]) + "g")
        print("Money:  $" + str(tot_mon))
    if order != "espresso" and order != "latte" and order != "cappuccino" and order != "off" and order != "report":
        print("That's not an acceptable input! Sorry.")
        break
    can_make = False
    if order == "espresso":
        esp_wtr = menu["espresso"]["ingredients"]["water"]
        esp_cfe = menu["espresso"]["ingredients"]["coffee"]
        if resources["water"] - esp_wtr >= 0 and resources["coffee"] - esp_cfe >= 0:
            can_make = True
            resources["water"] -= esp_wtr
            resources["coffee"] -= esp_cfe
        elif resources["water"] - esp_wtr < 0:
            print("Sorry, there is not enough water!")
        elif resources["coffee"] - esp_cfe < 0:
            print("Sorry, there is not enough coffee!")

    elif order == "latte":
        lte_wtr = menu["latte"]["ingredients"]["water"]
        lte_mlk = menu["latte"]["ingredients"]["milk"]
        lte_cfe = menu["latte"]["ingredients"]["coffee"]
        if resources["water"] - lte_wtr > 0 and resources["coffee"] - lte_cfe > 0 and resources["milk"] - lte_mlk > 0:
            can_make = True
            resources["water"] -= lte_wtr
            resources["coffee"] -= lte_cfe
            resources["milk"] -= lte_mlk
        elif resources["water"] - lte_wtr < 0:
            print("Sorry, there is not enough water!")
        elif resources["coffee"] - lte_cfe < 0:
            print("Sorry, there is not enough coffee!")
        elif resources["milk"] - lte_mlk < 0:
            print("Sorry, there is not enough milk!")

    elif order == "cappuccino":
        cap_wtr = menu["cappuccino"]["ingredients"]["water"]
        cap_mlk = menu["cappuccino"]["ingredients"]["milk"]
        cap_cfe = menu["cappuccino"]["ingredients"]["coffee"]
        if resources["water"] - cap_wtr > 0 and resources["coffee"] - cap_cfe > 0 and resources["milk"] - cap_mlk > 0:
            can_make = True
            resources["water"] -= cap_wtr
            resources["coffee"] -= cap_cfe
            resources["milk"] -= cap_mlk
        elif resources["water"] - cap_wtr < 0:
            print("Sorry, there is not enough water!")
        elif resources["coffee"] - cap_cfe < 0:
            print("Sorry, there is not enough coffee!")
        elif resources["milk"] - cap_mlk < 0:
            print("Sorry, there is not enough milk!")

    if can_make:
        print("Please insert coins.")
        usr_tot = 0.0
        change = 0.0
        qt = int(input("How many quarters: "))
        dme = int(input("How many dimes: "))
        nkl = int(input("How many nickels: "))
        pny = int(input("How many pennies: "))
        for i in range(qt):
            usr_tot += 0.25
        for i in range(dme):
            usr_tot += 0.1
        for i in range(nkl):
            usr_tot += 0.05
        for i in range(pny):
            usr_tot += 0.01
        if usr_tot >= menu[order]["cost"]:
            change = usr_tot - menu[order]["cost"]
            tot_mon += menu[order]["cost"]
            if change == 0:
                print("Here is your " + order + ", enjoy!")

            if change > 0:
                print("Here is $" + str(round(change,2)) + " in change.")
                print("Here is your " + order + ", enjoy!")

        else:
            print("Sorry that's not enough money. Money refunded.")
    if resources["water"] <= 0 or resources["coffee"] <= 0 or resources["milk"] <= 0:
        more_resources = False
        print("The coffee machine is out of some ingredients, sorry for the inconvenience!")

