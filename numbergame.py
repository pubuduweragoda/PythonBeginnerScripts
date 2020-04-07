# this program is a number guessing game

import random


#Get the user name in one line
name = str(input('What is your name?'))


# Check if the user entered a valid value
def check_if_valid():
      # "guess" only exists inside "check_if_valid"
      while(True):
          try: guess = int(input('Well, ' + name + ' I am thinking of a number between 1 and 100. What do you think it is?'))
      except ValueError:
          print('That is not a valid number. Try again')
          pass
      else:
          break


# call "check_if_valid()" and store the guessed value in "user_guess"
user_guess = check_if_valid()


# Generate random number (number that the computer is thinking
realNum = random.randint(1,100)


# Counts the number of attempts by the user
i = 1


# Check if, guessed number = computer generated number
while (guess != realNum):
    if int(guess) == int(realNum):
        print('Good job! It only took you ' + str(i) + ' tries.')
    if int(guess) < int(realNum):
        print('No, that is too low. Try again.')
    elif int(guess) > int(realNum):
        print('No, that is too high. Try again.')
    guess = input()
    i += 1
