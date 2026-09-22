import random

game_number = random.randint(1,10)
guess_count = 0

while(True):

    guess = int(input("Guess a number between 1 and 10: "))
    guess_count += 1

    if guess > game_number:
        print("Boooo too high")
    elif guess < game_number: 
        print("Boooo too low")
    else:
        if guess_count == 1:
            comment = "Amazing! You got it on the first try!"
        elif guess_count <= 3:
            comment = "Great job! You were quick."
        elif guess_count <= 6:
            comment = "Nice work! You got it in a decent number of guesses."
        else:
            comment = "You finally got it! Maybe next time you'll do even better."
        print(f"You win!! It took you {guess_count} guesses.")
        print(comment)
        break