# this program is a number guessing game

import random

print('What is your name?')
name = str(input())
print('Well, ' + name + ' I am thinking of a number between 1 and 100. What do you think it is?')
try: guess = int(input())
except ValueError:
    print('That is not an number. Try again')
    guess = int(input)
realNum = random.randint(1,100)

i = 1

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



