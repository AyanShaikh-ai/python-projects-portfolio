from coffe_machine_info import MENU, resources

def report():
    print(f"\n water: {resources["water"]} \n milk: {resources["milk"]} \n coffee: {resources["coffee"]} \n money: {resources["money"]}")


def resource_check(drink_name):
    ingredients = MENU[drink_name]["ingredients"]

    for items in ingredients:
        if ingredients[items] > resources[items]:
            print(f"sorry there is not enough {items}")
            return False

    return True

def calc_user_money(one,five,ten,twentyfive):
    total_money = (one * 0.01) + (five * 0.05) + (ten * 0.10) + (twentyfive * 0.250)
    return total_money

def money_check(drink_name,u_money):
    cost = MENU[drink_name]["cost"]
    if u_money == cost:
        resources["money"] += cost
        return True
    elif u_money > cost:
        resources["money"] += cost
        change = round(u_money - cost, 2)
        print(f"here is your change: £{change}")
        return True
    elif u_money < cost:
       print(f"sorry not enough money, £{u_money} will be refunded.")
       return False

def new_machine_resources(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    for items in ingredients:
        resources[items] -= ingredients[items]



is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "report":
        report()
        continue
    if user_input == "off":
        is_on = False
        continue

    if user_input not in MENU and user_input not in ["report", "off"]:
        print("Invalid choice.")
        continue

    resource_sufficient = resource_check(user_input)
    if resource_sufficient:
        print("Please insert coins")
        twentyfivepcoins = int(input("how many 25p coins?: "))
        tenpcoins = int(input("how many 10p coins?: "))
        fivepcoins = int(input("how many 5p coins?: "))
        pennies = int(input("how many pennies?: "))
        user_money = calc_user_money(pennies,fivepcoins,tenpcoins,twentyfivepcoins)
        enough_money = money_check(user_input, user_money)

        if enough_money:
            print(f"here is your {user_input}, Enjoy!")
            new_machine_resources(user_input)

        else:
            continue




