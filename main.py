import random

game_number = random.randint(1,10)
print(game_number)

while(True):

    guess = int(input("Guess a number between 1 and 10: "))

    if guess > game_number:
        print("Boooo too high")
    elif guess < game_number: 
        print("Boooo too low")
    else:
        print("You win!!")
        break