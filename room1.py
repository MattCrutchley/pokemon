from pokemon import pokemon
from battle import battle
import random
import time

def room1(your_pokemon):
    cmd = ""
    while cmd != "r":
        #commands = "s to search for wood\nr to return home\n"
        print("you enter the woods, what would you like to do?")
        cmd = input("s to search for wood\ni to display inventory\nr to return home\n")
        if cmd.lower() == "s":
            print("Searching....")
            outcome = random.randint(0,10)
            if outcome < 3:
                print( "you are attacked")
                result = battle(your_pokemon)
                if result == "killed":
                    break
            elif outcome < 7:
                print( "you find nothing search again?")
            else:
                your_pokemon.inventory.update(wood = your_pokemon.inventory["wood"] + 1)
                print(your_pokemon.inventory["wood"])
                print("you found wood, this has been added to your inventory")
        elif cmd.lower() == "r":
            print("returning home")
        elif cmd.lower() == "i":
            print(your_pokemon.inventory)
        else:
            print("command not recognised")