from room1 import room1
from room2 import room2
from pokemon import player, pokemon
from battle import battle

rooms = ["woods", "cliff"]
starter_choices = [["mage", 100,60,80,"mage"],["melee",100,80,60,"melee"],["range",100,80,60,"range"]]
spec = ["HP","Attack","Defence","Type"]
smoke = 0
xp = 0
inventory = {"wood": 0, "rope": 0}

choice = input("choose your wepon\n %s \n %s \n %s \n or \n %s \n %s \n %s \nor \n %s \n %s \n %s \n\n" %(starter_choices[0][0],spec, starter_choices[0][1:],starter_choices[1][0], spec,starter_choices[0][1:],starter_choices[2][0], spec,starter_choices[0][1:]))

if choice == "mage":
    your_pokemon = player(choice,100, 60, 80, "mage",inventory,xp)   
elif choice == "melee":
    your_pokemon = player(choice,100, 80, 60,"melee",inventory,xp)
else:
    print("choice not recognised")

while your_pokemon.hp > 0:

    room_choice = input("choose a destination %s \n" %(rooms))

    if room_choice == rooms[0]:
        room1(your_pokemon)
    elif room_choice == rooms[1]:
        room2(your_pokemon)


print("--------------------\nGAME OVER\n----------------------")

print("testing stats")
print(your_pokemon.inventory["wood"])
print(your_pokemon.xp)


