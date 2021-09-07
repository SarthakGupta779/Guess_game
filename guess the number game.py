import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("enter your guess number : "))
    guesses = guesses + 1
    if(userGuess==randNumber):
        print("your guessed is right : ")
    else:
        if(userGuess>randNumber):
            print("your guess is wrong! Enter a smaller Number :  ")
        else:
            print("your guess is wrong! Enter a larger  Number :  ")

print(f"your guesses the number in {guesses} guesses")

with open("hiscore.txt" , "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("you have just broken the hiscore! ")
with open("hiscore.txt" , "w") as f:
        f.write(str(guesses))