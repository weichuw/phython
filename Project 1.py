import random

games = ''

while games == '' :
    try:
        games = int(input("How many games do you want to play?"))
        
    except:
        print("Please select a number betwen 1-25")
        
for game in range(0,games):
    pick = random.randint(1,25)
    guess = None
    attemps = 0
    
    while pick != guess :
        try:
            guess = int(input("Pick a number:"))
        except:
            print("Please select a number")
            continue
        
        if guess != pick:
            attemps += 1
            if guess > pick:
                print("Too high")
            else:
                print("Too low")
        else:
            print("Correct: It took you this many attemps: %s" % attemps)
            