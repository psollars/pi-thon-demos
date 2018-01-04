import random
import time

def roll_the_die():
    global keep_rolling
    response = input("Would you like to roll a die? Enter Y or N\n")
    if response.lower() == "n":
        keep_rolling = False
    elif response.lower() == "y":
        keep_rolling = True
    else:
        print("Hey, you gotta enter Y or N.")
        time.sleep(1.5)
        roll_the_die()
        
keep_rolling = True
while keep_rolling == True:
    roll_the_die()
    if keep_rolling == True:
        print("You roll a die...")
        time.sleep(1.5)
        print("It's a", random.randint(1,6))
    else:
        break
    
