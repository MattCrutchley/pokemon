class pokemon:
    def __init__(self,name,hp,attack,defence,type_):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.type_ = type_

    def calculate_damage(self,your_type, opponent_type, attack, defense, xp):
        effectivness = 0
    
        dicts = [{"mage":{"melee":2,"range":0.5,"mage":1}},
        {"range":{"mage":2,"melee":0.5,"range":0.5}},
        {"melee":{"mage":0.5,"range":2,"melee":1}}]
    
        if your_type == opponent_type:
            effectivness = 0.5
        else:       
            for item in dicts:
                for j in item:
                    if j == your_type:
                        effectivness = item[your_type][opponent_type]      
       

        return 50 * (attack / defense) * effectivness + xp

class player(pokemon):
    def __init__(self,name,hp,attack,defence,type_,inventory,xp,equipped):
        super().__init__(name,hp,attack,defence,type_)
        self.inventory = inventory = {"wood": 0, "rope": 0, "vines":10,"bow":0,"stone":0,"arrow":0,"fruit":0,"wooden sword":0}
        self.xp = 0
        self.equipped = "none"


#def defence(self,defence_type,attack_type):
 #   if         
