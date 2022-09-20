import random

print('\n\n')
print("**** Welcome to The Perfect Guess game ****\n\n")

print("The computer has generated a random number(1 - 100) :")
randNumber = random.randint(1, 100)

userGuess = None
guesses = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter your guessed number:  "))
    guesses += 1

    if userGuess == randNumber:
        print("Your guess is correct one...\n")

    elif (userGuess > randNumber):
        print('The number you have guessed is high, please guess lower\n')

    else:
        print('The number you have guessed is low, please guess higher\n')

print(f'You have guessed the number in {guesses} guesses...\n')

with open('HighScore.txt', 'r') as f:
    highScore = int(f.read(guesses))
    
if (guesses<highScore):
    print("Congratulations!!! You've just broken the highscore...")
    with open('HighScore.txt', 'w') as f:
        f.write(str(guesses))
