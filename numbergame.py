# this program is a number guessing game

import random


#Get the user name in one line
name = str(input('What is your name?'))


print('Well, ' + name + ' I am thinking of a number between 1 and 100. What do you think it is?')


# Check if the user entered a valid value
while(True):
  try: guess = int(input())
  except ValueError:
      print('That is not a valid number. Try again')
      pass
  else:
      break


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

print('Good job! It only took you ' + (i+1) + ' tries.')



