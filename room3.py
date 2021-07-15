def room3(your_pokemon):
    crafts = [{"bow":{"wood":1,"vines":1}},
          {"10 arrows":{"wood":2,"stone": 1}}
         ]
    cmd = ""
    while cmd != "r":
        #commands = "s to search for wood\nr to return home\n"
        print("This is where you can craft items if you have the right resources\n")
        print(print(your_pokemon.inventory))
        print(crafts)
        cmd = input("enter the name of an item to make")
        print(crafts[0]["bow"])
        key_list = [key for key in crafts[0][cmd]]
        print(key_list)
        for resource in key_list:
            print(crafts[0][cmd][resource])
            if your_pokemon.inventory[resource] < crafts[0][cmd][resource]:
                print("you dont have enough %s for that" %(resource))
            else:
                your_pokemon.inventory[resource] = your_pokemon.inventory[resource] - crafts[0][cmd][resource]
                your_pokemon.inventory[resource] = your_pokemon.inventory[resource] + 1
                print(your_pokemon.inventory)


 
