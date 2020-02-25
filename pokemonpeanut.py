from pokemon import pokemon
import random
import time
starter_choices = [["big bad bob", 100,60,80,"water"],["wheres my whey jay",100,80,60,"fire"]]
spec = ["HP","Attack","Defence","Type"]
print(starter_choices[0][0])

choice = input("choose your wepon\n %s \n %s \n %s \n or \n %s \n %s \n %s \n\n" %(starter_choices[0][0],spec, starter_choices[0][1:],starter_choices[1][0], spec,starter_choices[0][1:]))

if choice == "big bad bob":
    your_pokemon = pokemon(choice,100, 60, 80, "water")   
elif choice == "wheres my whey jay":
    your_pokemon = pokemon(choice,100, 80, 60,"fire")
else:
    print("choice not recognised")

battle = random.randint(0,1)
enemies = [["big bad tadas",100,60,80,"grass"],["a wandering idiot",100, 80, 60,"water"]]


opponent_pokemon = pokemon(enemies[battle][0],enemies[battle][1],enemies[battle][2],enemies[battle][3],enemies[battle][4])
print("\n%s type %s wants to battle! \n" %(enemies[battle][0],enemies[battle][4]))
 
battle_option = input("R to run or F to fight! ")
if battle_option.lower() == "r":
    print("\nyou ran away")
else:
    while getattr(your_pokemon, "hp") > 0:
        cmd = input("\npress x to attack or s smokescreen")
        # attack
        if cmd.lower() == "x":
            damage = your_pokemon.calculate_damage(getattr(your_pokemon,"type_"),getattr(opponent_pokemon,"type_"),random.randint(1,50),random.randint(1,50))
            print("\ndamage %.2f \n " %(damage))
            setattr(opponent_pokemon,"hp",getattr(opponent_pokemon,"hp") - damage)
            if getattr(opponent_pokemon,"hp") <= 0:
                print("you killed ", opponent_pokemon.name,"\n")
            else:
                print("opponents hp: %.2f " %(getattr(opponent_pokemon,"hp")),"\n")    

        elif cmd.lower() == "s":
            smoke = randint(0,4)
            if smoke > 2:
                print("%s is paralysed" %(getattr(opponent_pokemon,"name"))
            else:    
                print("%s evaded your attack"%(getattr(opponent_pokemon,"name"))
        
        time.sleep(1)

        if smoke <= 2:
            smoke = 0
            #opponent attack
            print("\n-------------------------------------------------------------------\n")
            op_damage = opponent_pokemon.calculate_damage(getattr(opponent_pokemon,"type_"),getattr(your_pokemon,"type_"),random.randint(1,50),random.randint(1,50))

            setattr(your_pokemon,"hp",getattr(your_pokemon,"hp") - op_damage)
            print("you are attacked, you loose %.2f " %(damage),"HP!\n")
            if getattr(your_pokemon,"hp") <= 0:
                print("%s killed you\n" %(enemies[battle][0]))
            else:    
                print("your hp: %.2f "%(getattr(your_pokemon,"hp")),"\n")
            print("\n-------------------------------------------------------------------\n")   
        


