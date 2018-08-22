import random

print ("***********************************************")
print ("*            Guess the number app             *")
print ("***********************************************")

playagain = True
while playagain :
    gameover = False
    mynumber: object = random.randint(1,100)
    print ("the number we are going for is : {}", mynumber)
    print ("lets start")

    while not gameover:
        s = input ('What is your guess ? ')
        number = int(s)
        if (number < mynumber):
            print ("too small!")
        elif (number > mynumber):
            print ("too big")
        else:
            print ("Great job!")
            gameover = True
    yesno = input ("That was fun!. Want to play again? [yes/no]: ")
    yesno = yesno.strip()
    if not (yesno) :
        print ("You have to enter yes or no. Assuming 'no'. good bye")
        yesno = "no"
    yesno: str = yesno.lower()
    print()

    if (yesno == "no"):
        playagain = False