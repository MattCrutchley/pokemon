from pokemon import pokemon
from functions import find_opponent, attack
import random
import time
commands = "x to attack\ns to smokescreen\nr to run"
starter_choices = [["big bad bob", 100,60,80,"water"],["wheres my whey jay",100,80,60,"fire"]]
spec = ["HP","Attack","Defence","Type"]
smoke = 0
choice = ""
xp = 0

while choice !="big bad bob" or "wheres my whey jay":
    choice = input("choose your wepon\n %s \n %s \n %s \n or \n %s \n %s \n %s \n\n" %(starter_choices[0][0],spec, starter_choices[0][1:],starter_choices[1][0], spec,starter_choices[0][1:]))

    if choice == "big bad bob":
        your_pokemon = pokemon(choice,100, 60, 80, "water")
        break   
    elif choice == "wheres my whey jay":
        your_pokemon = pokemon(choice,100, 80, 60,"fire")
        break
    else:
        print("\nchoice not recognised\n")



battle = random.randint(0,1)
enemies = [["big bad tadas",100,60,80,"grass"],["Random man",100, 80, 60,"water"]]


opponent_pokemon = ()
 
battle_option = input("R to run or F to fight! ")
if battle_option.lower() == "r":
    print("\nyou ran away")
else:
    while getattr(your_pokemon, "hp") > 0:

        cmd = input("\nenter command (cmd to show commands) ")
        # attack
        while cmd.lower() == "cmd":
            print(commands)       
            cmd = input("\nenter command (cmd to show commands) ")

        if cmd.lower() == "x":
            smoke = 0
            attack(your_pokemon, opponent_pokemon,xp)
            
    
        elif cmd.lower() == "s":
            smoke = random.randint(0,4)                       
            if smoke > 2:
                print("\n%s is paralysed" %(getattr(opponent_pokemon,"name")))
            else:
                print("\n%s evaded your attack" %(getattr(opponent_pokemon,"name")))   
       
        elif cmd.lower() == "r":
            print("you ran away")
            break  
        else:
            print("\n command not recognised")     

        time.sleep(2)
        print("\n-------------------------------------------------------------------\n")
        if smoke <= 2:
            smoke = 0
            #opponent attack

            op_damage = opponent_pokemon.calculate_damage(getattr(opponent_pokemon,"type_"),getattr(your_pokemon,"type_"),random.randint(1,50),random.randint(1,50))

            setattr(your_pokemon,"hp",getattr(your_pokemon,"hp") - op_damage)
            print("you are attacked, you loose %.2f " %(op_damage),"HP!\n")
            if getattr(your_pokemon,"hp") <= 0:
                print("%s killed you\n" %(enemies[battle][0]))
            else:    
                print("your hp: %.2f "%(getattr(your_pokemon,"hp")),"\n")
            print("\n-------------------------------------------------------------------\n")   
        else:
            print("\n%s is still paralysed" %(getattr(opponent_pokemon,"name")))


