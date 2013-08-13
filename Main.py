import string
import random

solution = random.randint(0,100)


win = False
guesslast = 0
guess = 0
tries = 0

while win is False:
    guesslast = guess
    guess = int(input("pick a number"))
    if guess<solution:
        print("Go Higher")
        tries+=1
    if guess>solution:
        print("Go Lower")
        tries+=1
    if guess==solution:
        print("winner!")
        win = True
print("it only took " + str(tries) + " tries")
input("Press any key to quit")