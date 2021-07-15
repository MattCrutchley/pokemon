from pokemon import pokemon
from battle import battle
import random
import time

def room1(your_pokemon):
    cmd = ""
    items=["wood","vines","stone"]
    while cmd != "r":
        #commands = "s to search for wood\nr to return home\n"
        print("you enter the woods, what would you like to do?\n")
        cmd = input("s to search \ni to display inventory\nr to return home\n")
        if cmd.lower() == "s":
            print("Searching....\n")
            outcome = random.randint(0,10)
            if outcome < 3:
                print( "you are attacked\n")
                result = battle(your_pokemon)
                if result == "killed":
                    break
            elif outcome < 7:
                print( "you find nothing search again?\n")
            else:
                find_index = random.randint(0,len(items)-1)
                find=items[find_index]
                your_pokemon.inventory[find] = your_pokemon.inventory[find] + 1
                print(your_pokemon.inventory[find])
                print("you found %s, this has been added to your inventory\n"%(find))
        elif cmd.lower() == "r":
            print("returning home\n")
        elif cmd.lower() == "i":
            print(your_pokemon.inventory)
        else:
            print("command not recognised")