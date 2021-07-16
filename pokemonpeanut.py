from room1 import room1
from room2 import room2
from room3 import room3
from pokemon import player, pokemon


rooms = ["woods", "cliff", "craft"]
starter_choices = [["mage", 100,60,80,"mage"],["melee",100,80,60,"melee"],["range",100,80,60,"range"]]
spec = ["HP","Attack","Defence","Type"]
smoke = 0
xp = 0
inventory = {"wood": 0, "rope": 0, "vines":10,"bow":0,"stone":0,"arrow":0,"fruit":0,"wooden sword":0}

choice = input("choose your wepon\n %s \n %s \n %s \n or \n %s \n %s \n %s \nor \n %s \n %s \n %s \n\n" %(starter_choices[0][0],spec, starter_choices[0][1:],starter_choices[1][0], spec,starter_choices[0][1:],starter_choices[2][0], spec,starter_choices[0][1:]))

if choice == starter_choices[0][0] or starter_choices[1][0] or starter_choices[2][0]:
    your_pokemon = player(choice,100, 60, 80, choice,inventory,xp,"none")
else:
    print("choice not recognised")

while your_pokemon.hp > 0:

    room_choice = input("choose a destination %s \n" %(rooms))
    if your_pokemon.inventory["wooden sword"] > 0:
        print("wooden sword equipped, adds20 points to attack....")
        your_pokemon.attack = your_pokemon.attack + 2

    if room_choice == rooms[0]:
        room1(your_pokemon)
    elif room_choice == rooms[1]:
        result = room2(your_pokemon)
        if result == "climbed":
            print("-----------------\n NEW LEVEL \n --------------")
            break
    elif room_choice == rooms[2]:
        room3(your_pokemon)


print("--------------------\nGAME OVER\n----------------------")

print("testing stats")
print(your_pokemon.inventory["wood"])
print(your_pokemon.xp)


