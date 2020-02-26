from pokemon import pokemon
import random

def find_opponent():
    battle = random.randint(0,1)
    enemies = [["big bad tadas",100,60,80,"grass"],["Random man",100, 80, 60,"water"]]
    opponent_pokemon = pokemon(enemies[battle][0],enemies[battle][1],enemies[battle][2],enemies[battle][3],enemies[battle][4])
    print("\n%s type %s wants to battle! \n" %(enemies[battle][0],enemies[battle][4]))
    return opponent_pokemon


def attack(your_pokemon, opponent_pokemon):
    damage = your_pokemon.calculate_damage(getattr(your_pokemon,"type_"),getattr(opponent_pokemon,"type_"),random.randint(1,50),random.randint(1,50))
    print("\ndamage %.2f \n " %(damage))
    setattr(opponent_pokemon,"hp",getattr(opponent_pokemon,"hp") - damage)
    if getattr(opponent_pokemon,"hp") <= 0:
        print("you killed ", opponent_pokemon.name,"\n")
        xp += 1
        print("you gained 1 XP!\nyour XP is now %s"%(xp))
        

def smokescreen(opponent_pokemon):
    smoke = random.randint(0,4)                       
    if smoke > 2:
        print("\n%s is paralysed" %(getattr(opponent_pokemon,"name")))
    else:
        print("\n%s evaded your attack" %(getattr(opponent_pokemon,"name")))