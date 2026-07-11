import random
playing = True
number = str(random.randint(0, 9))
print("I will generate a number from 0 to 9. You have to guess it.")
print("the game ends when you get 1 hero")
while playing:
    guess = input("Enter your guess! \n")
    if number == guess:
        print("You guessed it right! The number was " + number)
        playing = False
    else:
        print("Wrong guess. Try again!")