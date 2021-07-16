def room3(your_pokemon):
    crafts = [{"wooden sword":{"wood":3,"stone":1}},
          {"cooked meal":{"wood":1,"food": 1}},
          {"rope":{"vines":10}}
         ]
    cmd = ""
    while cmd != "r":
        #commands = "s to search for wood\nr to return home\n"
        print("This is where you can craft items if you have the right resources...\n")
        print("This is your current inventory:\n")
        print(your_pokemon.inventory)
        print("These are items to craft:\n")
        print(crafts)
        cmd = input("\n enter the name of an item to make or r to return home  \n")
        if cmd.lower() == "r":
            break
        count = 0
        cannotafford=0
        costs = []
        cost_amounts = []
        match = 0
        cost_count = 0
        for item in crafts:
            
            for j in item:
                if j == cmd:
                    print("Your item is a %s" %(j))
                    match = 1      
                    print("This will cost ")
                    print(crafts[count][cmd])
                    for resource in crafts[count][j]:
                        print("resource: %s" %(resource))
                        print(crafts[count][j][resource])
                        print("you have")
                        print(your_pokemon.inventory[resource])
                        if your_pokemon.inventory[resource] < crafts[count][j][resource]:
                            cannotafford=1
                        else:
                            costs.append(resource)
                            cost_amounts.append(crafts[count][j][resource])
                            purchace = j                          
                count += 1
        if match == 0:
            print("this item does not exist")
        elif cannotafford == 1:
            print("CANNOT AFFORD ITEM")
        else:
            print("\n removing %s from inventory \n" %(costs))
            for cost in costs:
                your_pokemon.inventory[cost] = your_pokemon.inventory[cost] - cost_amounts[cost_count]
                cost_count += 1
            print("\n adding %s to inventory \n" %(purchace))
            your_pokemon.inventory[purchace] = your_pokemon.inventory[purchace] + 1
            

 
