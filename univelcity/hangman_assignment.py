import random


file = open ('twist.txt' , 'r')
for x in file:
    words = x.split(" ")

wordIndex = random.randint(0, len(words) - 1)

getRandomWord = words[wordIndex]

print('Hello! What is your name?')

myName = input()

print('Welcome , ' + myName )
print('Start HANGMAN ? (yes or no)')

play = input()

if play == 'yes':


    print('H A N G M A N')

    missedLetters = ''

    correctLetters = ''

    secretWord = getRandomWord

    gameIsDone = False


    while gameIsDone == False:

        print(len(missedLetters))

        print()



        print('Missed letters:', end=' ')

        for letter in missedLetters:

            print(letter, end=' ')

        print()



        blanks = '_' * len(secretWord)



        for i in range(len(secretWord)): # replace blanks with correctly guessed letters

            if secretWord[i] in correctLetters:

                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]



        for letter in blanks: # show the secret word with spaces in between each letter

            print(letter, end=' ')

        print()



        #  Let the player type in a letter.

        # while True:

        print('Guess a letter.')

        guess = input()

        guess = guess.lower()

        alreadyGuessed = [guess]

        if len(guess) != 1:

            print('Please enter a single letter.')

        elif x in guess:

            print('You have already guessed that letter. Choose again.')

        elif guess not in 'abcdefghijklmnopqrstuvwxyz':

            print('Please enter a LETTER.')

        else:

            alreadyGuessed = [alreadyGuessed.append(guess)]





else: print('Are you for real')

# while play == 'yes':

    # print('Do you want to play again? (yes or no)')

    # playAgain = input().lower().startswith('y')

   





# print(getRandomWord)
