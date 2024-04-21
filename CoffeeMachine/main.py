import time


def user_way_out():
    print('')


# money
quarters = float(0.25)
dimes = float(0.10)
nickles = float(0.5)
pennies = float(0.01)

# resources
resource_water = 300
resource_milk = 200
resource_coffee = 100
resource_money = 0

# espresso
espresso_water = 50
espresso_milk = 0
espresso_coffee = 18
espresso_cost = 1.5

# latte
latte_water = 200
latte_milk = 150
latte_coffee = 24
latte_cost = 2.5

# cappuccino
cappuccino_water = 250
cappuccino_milk = 100
cappuccino_coffee = 24
cappuccino_cost = 3.0


def resources_left():
    print('These are the resources now:')
    print('Water', resource_water)
    print('Milk', resource_milk)
    print('Coffee', resource_coffee)
    print('Money', resource_money)


while True:
    user_order = input('What would you like? (espresso/latte/cappuccino): ')
    if user_order == 'off':
        exit()
    if user_order == 'report':
        resources_left()

    if user_order == 'latte':
        if resource_water - latte_water > 0 and resource_milk - latte_milk > 0 and resource_coffee - latte_coffee > 0:
            print('Please insert $2.50')
            inserted_quarters = float(input('quarters: '))
            inserted_dimes = float(input('dimes: '))
            inserted_nickles = float(input('nickles: '))
            inserted_pennies = float(input('pennies: '))

            quarters_pay = inserted_quarters * float(quarters)
            dimes_pay = inserted_dimes * float(dimes)
            nickles_pay = inserted_nickles * float(nickles)
            pennies_pay = inserted_pennies * float(pennies)

            total_payed = pennies_pay + nickles_pay + dimes_pay + quarters_pay
            total_payed = total_payed - latte_cost

            while total_payed < latte_cost:
                print('That\'s not enough money.')
                print('Money refunded')
                print('Try again.')
                print('')
                time.sleep(1)
                inserted_quarters = float(input('quarters: '))
                inserted_dimes = float(input('dimes: '))
                inserted_nickles = float(input('nickles: '))
                inserted_pennies = float(input('pennies: '))
                quarters_pay = inserted_quarters * float(quarters)
                dimes_pay = inserted_dimes * float(dimes)
                nickles_pay = inserted_nickles * float(nickles)
                pennies_pay = inserted_pennies * float(pennies)
                total_payed = pennies_pay + nickles_pay + dimes_pay + quarters_pay
                total_payed = total_payed - latte_cost

            total_payed = total_payed - latte_cost
            resource_water = resource_water - latte_water
            resource_coffee = resource_coffee - latte_coffee
            resource_milk = resource_milk - latte_milk
            resource_money = resource_money + latte_cost
            print('')
            print('Working on it...')
            # TODO: let the text flow in while waiting for your coffee
            # look in the replit code
            time.sleep(2)
            print('')
            print('')
            print('You got your Latte.')
            print('You got $', round(total_payed, 2), 'back.')
            time.sleep(2)
            print('')
            resources_left()

        else:
            print('Sorry there are not enough resources left.')

    elif user_order == 'cappuccino':
        if resource_water - cappuccino_water > 0 and resource_milk - cappuccino_milk > 0 and \
                resource_coffee - cappuccino_coffee > 0:
            print('Please insert $3')
            inserted_quarters = float(input('quarters: '))
            inserted_dimes = float(input('dimes: '))
            inserted_nickles = float(input('nickles: '))
            inserted_pennies = float(input('pennies: '))

            quarters_pay = inserted_quarters * float(quarters)
            dimes_pay = inserted_dimes * float(dimes)
            nickles_pay = inserted_nickles * float(nickles)
            pennies_pay = inserted_pennies * float(pennies)

            total_payed = pennies_pay + nickles_pay + dimes_pay + quarters_pay
            total_payed = total_payed - cappuccino_cost

            while total_payed < cappuccino_cost:
                print('That\'s not enough money.')
                print('Money refunded')
                print('Try again.')
                print('')
                time.sleep(1)
                inserted_quarters = float(input('quarters: '))
                inserted_dimes = float(input('dimes: '))
                inserted_nickles = float(input('nickles: '))
                inserted_pennies = float(input('pennies: '))
                quarters_pay = inserted_quarters * float(quarters)
                dimes_pay = inserted_dimes * float(dimes)
                nickles_pay = inserted_nickles * float(nickles)
                pennies_pay = inserted_pennies * float(pennies)
                total_payed = pennies_pay + nickles_pay + dimes_pay + quarters_pay
                total_payed = total_payed - cappuccino_cost

            total_payed = total_payed - cappuccino_cost
            resource_water = resource_water - cappuccino_water
            resource_coffee = resource_coffee - cappuccino_coffee
            resource_milk = resource_milk - cappuccino_milk
            resource_money = resource_money + cappuccino_cost
            print('')
            print('Working on it...')
            time.sleep(2)
            print('')
            print('')
            print('You got your Cappuccino.')
            print('You got $', round(total_payed, 2), 'back.')
            time.sleep(2)
            print('')
            resources_left()

        else:
            print('Sorry there are not enough resources left.')

    elif user_order == 'espresso':
        if resource_water - espresso_water > 0 and resource_coffee - espresso_coffee > 0:
            print('Please insert $1.50.')
            inserted_quarters = float(input('quarters: '))
            inserted_dimes = float(input('dimes: '))
            inserted_nickles = float(input('nickles: '))
            inserted_pennies = float(input('pennies: '))

            quarters_pay = inserted_quarters * float(quarters)
            dimes_pay = inserted_dimes * float(dimes)
            nickles_pay = inserted_nickles * float(nickles)
            pennies_pay = inserted_pennies * float(pennies)

            total_payed = pennies_pay + nickles_pay + dimes_pay + quarters_pay
            total_payed = total_payed - espresso_cost
            while total_payed < espresso_cost:
                print('That\'s not enough money.')
                print('Money refunded')
                print('Try again.')
                print('')
                time.sleep(1)
                inserted_quarters = float(input('quarters: '))
                inserted_dimes = float(input('dimes: '))
                inserted_nickles = float(input('nickles: '))
                inserted_pennies = float(input('pennies: '))
                quarters_pay = inserted_quarters * float(quarters)
                dimes_pay = inserted_dimes * float(dimes)
                nickles_pay = inserted_nickles * float(nickles)
                pennies_pay = inserted_pennies * float(pennies)
                total_payed = pennies_pay + nickles_pay + dimes_pay + quarters_pay
                total_payed = total_payed - espresso_cost

            total_payed = total_payed - espresso_cost
            resource_water = resource_water - espresso_water
            resource_coffee = resource_coffee - espresso_coffee
            resource_milk = resource_milk - espresso_milk
            resource_money = resource_money + espresso_cost
            print('')
            print('Working on it...')
            time.sleep(2)
            print('')
            print('')
            print('You got your Espresso.')
            print('You got $', round(total_payed, 2), 'back.')
            time.sleep(2)
            print('')
            resources_left()

        else:
            print('Sorry there are not enough resources left.')

    else:
        print('That is not a valid answer')
        print('Run the code again.')
        exit()

    time.sleep(4)
    print("")
    print("")
