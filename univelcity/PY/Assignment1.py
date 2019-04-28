import random

my_number = random.randint(1,5)
guess = 0
noOfguesses = 0

while guess != my_number :

    guess = int(input("i have a number, can you guess it? "))

    noOfguesses += 1

    if guess < my_number:

        print("you guessed number is below my number!")

    elif guess > my_number:

        print("you guessed number is above my number!")

    elif guess == my_number:

        print("you guessed right!")
        break
        
print(f"it took you {noOfguesses} guesses, to get my number")


    


