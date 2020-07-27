import time
import random

characters = ['dragon', 'monster', 'lion', 'bear', 'leopard',
              'vampire', 'serpent']

items = []


def print_pause(item):
    print(item)
    time.sleep(2)


def intro(enemy):
    print_pause("You hike up a mountain and see a majestic castle on your "
                "right.")
    print_pause("A dark and mysterious cave is in front of you.")
    print_pause("There is a small and creepy house on your left.")
    print_pause("Legend has it that there is a malicious " + enemy +
                " nearby.")
    print_pause("Where will you go?\n")


def choice(enemy):
    print_pause("Press 1 to go inside the castle.")
    print_pause("Press 2 to go inside the cave.")
    print_pause("Press 3 to go inside the house")
    response = input("(Please enter 1, 2, or 3)\n")
    if response == "1":
        castle(enemy)
    elif response == "2":
        cave(enemy)
    elif response == "3":
        house(enemy)
    else:
        choice(enemy)


def castle(enemy):
    print_pause("Once inside the castle you find the fierce " + enemy + ".")
    print_pause("The " + enemy + " attacks you!")
    while True:
        response = input("Press 1 to fight, press 2 to run away.\n")
        if response == "1":
            if "sheild" in items:
                print_pause("You pull out your bow and arrow along with the "
                            "sheild that you found in the cave.")
                print_pause("The " + enemy + " realizes that it is out "
                            "matched and flees the seen.")
                print_pause("Congratulatons! You have been victorious!")
                play_again()
                break
            else:
                print_pause("You fight the " + enemy + ".")
                print_pause("You try to kick it in the stomach, but it's "
                            "power and strength overwhelm you.")
                print_pause("You are defeated.")
                play_again()
                break
        elif response == "2":
            print_pause("You flee the " + enemy + " and run back out to the "
                        "feild.\n")
            choice(enemy)
            break


def cave(enemy):
    print_pause("You go inside the cave.")
    if "sheild" in items:
        print_pause("You have already been here inside the cave and gotten "
                    "everything inside, it is now just an empty cave.")
        print_pause("You go back to where you started.\n")
        choice(enemy)
    else:
        print_pause("Inside you find a bow and arrow along with a sheild.")
        items.append("sheild")
        print_pause("Now that you have found what's inside the cave you go "
                    "back to where you were.\n")
        choice(enemy)


def house(enemy):
    print_pause("You go into the house and you see dynamite on the floor.")
    print_pause("The dynamite looks like it might explode.")
    print_pause("Would you like to stay in the house or run away?\n")
    while True:
        response = input("Press 1 to stay or 2 to run.\n")
        if response == "1":
            print_pause("The dynamite explodes and consumes you!")
            print_pause("You died, game over.")
            play_again()
            break
        elif response == "2":
            print_pause("You run back out to the open.")
            print_pause("You breath a sigh of relief to be back out in the "
                        "open and away from the explosive house!\n")
            choice(enemy)
            break


def play_again():
    items.clear()
    response = input("Would you like to play again? 'Yes' or 'No'\n").lower()
    if response == "yes":
        play_game()
    elif response == "no":
        print_pause("Thanks for playing! Goodbye.")
    else:
        play_again()


def play_game():
    enemy = random.choice(characters)
    intro(enemy)
    choice(enemy)


play_game()
