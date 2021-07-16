from pokemon import pokemon
from battle import battle
import random
import time

def room2(your_pokemon):
    cmd = ""
    while cmd != "r":
        #commands = "s to search for wood\nr to return home\n"
        print("you approach a cliff, what would you like to do?")
        cmd = input("c to climb\ni to display inventory\nr to return home\n")
        if cmd.lower() == "c":
            if your_pokemon.inventory["rope"] == 0:
                cmd = input("you have no climbing rope, climbing without this is extremley dangerous, enter c to climb anyway or r to return home\n")
                if cmd.lower() == "c":
                    damage = random.randint(0,100)
                    if damage == 0:
                        print("you survived")
                        return "climbed"
                    else:
                        your_pokemon.hp = your_pokemon.hp - damage
                        print("you lost %s hp" %(damage))
                        if your_pokemon.hp <= 0:
                            print("you fell and died")
                            break
            else:
                print("you climb to the top of the cliff.....")
                return "climbed"
        elif cmd.lower() == "r":
            print("returning home")
        elif cmd.lower() == "i":
            print(your_pokemon.inventory)
        else:
            print("command not recognised")