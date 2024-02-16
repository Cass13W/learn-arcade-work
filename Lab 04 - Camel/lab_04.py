import random


def main():
    print("Welcome to Camel!")

    print("You stole a camel from a group of bandits to cross a huge desert.")

    print("The bandits want their camel back and are chasing you down to get their revenge!")

    print("Survive the desert and outrun the bandits.\n")

    # starting stats
    miles_traveled = 0
    thirst = 0
    camel_tired = 0
    native_traveled = -20
    canteen = 5
    natives_behind = miles_traveled - native_traveled
    done = False

    # main loop
    while not done:
        print("A. Drink from your canteen.")

        print("B. Ahead moderate speed.")

        print("C. Ahead full speed.")

        print("D. Stop for the night.")

        print("E. Status check.")

        print("Q. Quit or restart.")

        user_input = input("What is your choice?\n")

        # Quit or restart
        if user_input.lower() == "q":
            print("Are you sure you want to quit?")

            print("Y. Yes, quit.")

            print("N. No, restart game.")

            user_input = input("What is your choice?\n")

            if user_input.lower() == "y":
                done = True

            if user_input.lower() == "n":
                main()

        # check stats
        elif user_input.lower() == "e":
            print("You've traveled", miles_traveled, "miles.")

            print("You have", canteen, "sips of water left.")

            natives_behind = miles_traveled - native_traveled

            print("The bandits are", natives_behind, "miles behind you.\n")

        # stop and rest
        elif user_input.lower() == "d":
            print("You stop for the night.")

            print("Your camel is very happy about this decision.\n")

            camel_tired = 0

            native_traveled += random.randint(7, 14)

            natives_behind = miles_traveled - native_traveled

        # full speed
        elif user_input.lower() == "c":
            if camel_tired >= 15:

                print("Your camel is too tired to run.\n")

            else:
                print("Your camel runs at full speed.")

                full_speed = random.randint(10, 20)

                miles_traveled += full_speed

                camel_tired += random.randint(1, 3)

                thirst += 1

                native_traveled += random.randint(7, 14)

                natives_behind = miles_traveled - native_traveled

                print("You moved", full_speed, "miles.\n")

                oasis = random.randint(1, 20)

                # oasis chance
                if oasis == 20:
                    print("You found an oasis and refill your canteen.\n")

                    canteen = 5

                    thirst = 0

                    camel_tired = 0

                mirage = random.randint(1, 30)

                # mirage chance
                if mirage == 30:
                    print("You thought you saw an oasis, but it was just a mirage.")

                    print("Your camel disliked the detour.\n")

                    camel_tired -= 2

        # moderate pace
        elif user_input.lower() == "b":
            if camel_tired >= 15:

                print("Your camel is too tired to run.\n")

            else:
                print("Your camel runs at a moderate pace.")

                moderate_speed = random.randint(5, 12)

                miles_traveled += moderate_speed

                camel_tired += 1

                thirst += 1

                native_traveled += random.randint(7, 14)

                natives_behind = miles_traveled - native_traveled

                print("You moved", moderate_speed, "miles.\n")

                oasis = random.randint(1, 20)

                # oasis chance
                if oasis == 20:
                    print("You found an oasis and refill your canteen.\n")

                    canteen = 5

                    thirst = 0

                    camel_tired = 0

                mirage = random.randint(1, 30)

                # mirage chance
                if mirage == 30:
                    print("You thought you saw an oasis, but it was just a mirage.")

                    print("Your camel disliked the detour.\n")

                    camel_tired -= 2

        # drink
        elif user_input.lower() == "a":
            if canteen == 0:
                print("You are out of water.\n")

            else:
                print("You drink from your canteen.")

                canteen -= 1

                thirst = 0

                print("You have", canteen, "sips in your canteen left.\n")

        # invalid letter entered
        else:
            print("Please choose a valid letter.\n")

        # canteen empty
        if canteen == 0:
            print("You've run out of water.\n")

        # getting thirsty
        if thirst > 4 and thirst <= 6 and not done:
            print("You're getting thirsty, drink some water soon.\n")

        # died of thirst
        if thirst >= 6:
            print("You have died of dehydration.")

            print("Would you like to quit or restart?")

            print("Y. Quit.")

            print("N. Restart.")

            user_input = input("What is your choice?\n")

            if user_input.lower() == "y":
                done = True

            if user_input.lower() == "n":
                main()

        # camel getting tired
        if camel_tired > 10 and camel_tired <= 15 and not done:
            print("Your camel seems tired.\n")

        # camel collapses
        if camel_tired >= 15:
            print("Your camel has collapsed due to exhaustion.")

            print("The bandits easily catch up to you and take their revenge.")

            print("Would you like to quit or restart?")

            print("Y. Quit.")

            print("N. Restart.")

            user_input = input("What is your choice?\n")

            if user_input.lower() == "y":
                done = True

            if user_input.lower() == "y":
                main()

        # bandits are close
        if natives_behind <= 15:
            print("Better pick up the pace, the bandits are closing in!\n")

        # bandits catch up
        if natives_behind == 0:
            print("The bandits caught up to you and attacked you for stealing their camel.")

            print("Would you like to quit or restart?")

            print("Y. Quit.")

            print("N. Restart.")

            user_input = input("What is your choice?\n")

            if user_input.lower() == "y":
                done = True

            if user_input.lower() == "n":
                main()

        # win game
        if miles_traveled >= 200:
            print("You successfully escaped the bandits!")

            print("You and your stolen camel go on to live a happy life.")

            print("Would you like to quit or restart?")

            print("Y. Quit.")

            print("N. Restart.")

            user_input = input("What is your choice?\n")

            if user_input.lower() == "y":
                done = True

            if user_input.lower() == "n":
                main()


main()
