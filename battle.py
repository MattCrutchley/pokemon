from pokemon import pokemon
import random
import time

def battle(your_pokemon):
    commands = "x to attack\ns to smokescreen\nr to run"
    battle = random.randint(0,1)
    enemies = [["swamp lizard",100,60,80,"melee"],["giant spider",100, 80, 60,"melee"]]


    opponent_pokemon = pokemon(enemies[battle][0],enemies[battle][1],enemies[battle][2],enemies[battle][3],enemies[battle][4])
    print("\n%s type %s wants to battle! \n" %(enemies[battle][0],enemies[battle][4]))
 
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
                damage = your_pokemon.calculate_damage(getattr(your_pokemon,"type_"),getattr(opponent_pokemon,"type_"),random.randint(1,50),random.randint(1,50))
                print("\ndamage %.2f \n " %(damage))
                setattr(opponent_pokemon,"hp",getattr(opponent_pokemon,"hp") - damage)
                if getattr(opponent_pokemon,"hp") <= 0:
                    print("you killed ", opponent_pokemon.name,"\n")
                    your_pokemon.xp = your_pokemon.xp + 1
                    print("you gained 1 XP!\nyour XP is now %s"%(your_pokemon.xp))
                    return "won"
                else:
                    print("opponents hp: %.2f " %(getattr(opponent_pokemon,"hp")),"\n")    
            elif cmd.lower() == "s":
                smoke = random.randint(0,4)                       
                if smoke > 2:
                    print("\n%s is paralysed" %(getattr(opponent_pokemon,"name")))
                else:
                    print("\n%s is paralysed" %(getattr(opponent_pokemon,"name")))   
       
            elif cmd.lower() == "r":
                print("you ran away")
                return "flee"  
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

    return "killed"