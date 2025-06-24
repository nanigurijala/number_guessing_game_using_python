import random
from logo import logo
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def setDifficulty (chooseLevel) :
    if chooseLevel == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif chooseLevel == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
        
def checkNumber(guessNumber,answer,attempts):
    if guessNumber > answer:
        print('\nThe guess is too high')
        return attempts -1
    elif guessNumber < answer:
        print('\nThe guess is too low')
        return attempts -1
    else:
        print(f'\nyour guess is right.. the answer was {answer}')
        return attempts
        
def game():    
    print(logo)
    lowNumber = 1
    highNumber = 50

    answer = random.randint(lowNumber,highNumber)
    print(answer)
    print('Select a number between 1 and 50.')



    chooseLevel = input("\nChoose a level of difficult...Type 'easy' or 'hard': ").lower() 
    attempts = setDifficulty(chooseLevel)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print('\nYou entered a wrong level. Please type "easy" or "hard".')
        return
    guessNumber = 0

    while guessNumber != answer:
        print(f'\nyou have {attempts} attempts remaing to to guess the number.')
        guessNumber = int(input('Enter the guess number: '))

        attempts=checkNumber(guessNumber,answer,attempts)
        
        if attempts == 0:
            print(f'\nyour guesses are out .. you lost')
            return
        elif guessNumber != answer:
            print('Guess again')
        
           

game()