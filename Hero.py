
hero_stats = {
    "name" : "hero", # key : value (name -> key) : (hero -> value)
    "strength" : 7, 
    "Health" : 100.0,
}




def quit ():
    print ("You |Chose To Flee")
    print("Game Over")
    return False

def player_stats ():
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def player_move():
    pass

def player_pass():
    pass


isPlaying = True 

while (isPlaying):

    hero_stats["name"] = input ("\nWhat is Your Name?\n").lower()
    
    player_stats ()

    action = input ("\nSelect Action: Attack, Move or Flee\n").lower()

    print (f"Player Action:  {action}")

    if (action == "flee"):
        isPlaying = quit() #<-- is Playing = False
    elif (action == "attack"):
        player_attack()
    elif (action == move):
        player_move() 
    else:
        print(f"{action} invalid action")  
