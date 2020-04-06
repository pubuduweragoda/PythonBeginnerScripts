# rock paper scissor game

import time
import random
import sys

win = 0
lose = 0
tie = 0

# intro -- ask for name
print("Hi there! What's your name?\n")
name = input()
print('\nHey there, ' + str(name) + '! \n\nDo you want to play a game\
 of rock, paper, scissors? (yes/no)\n')

play = str(input())

if play.lower() == 'yes':
    print('\n\nOk! I will count down from three...\
\n\nThen you enter either \"rock\", \"paper\" \
or \"scissors\".')
    
elif play.lower() == 'no':
    print('\nBye!')
    sys.exit()
    
else:
    print('Hmm... Please enter /"yes/" or /"no/"')
    play = str(input())
    

time.sleep(3)        
# countdown
while play.lower() == 'yes':

    time.sleep(.5)
    print('\n3...')
    time.sleep(.5)
    print('\n2...')
    time.sleep(.5)
    print('\n1...\n')
    time.sleep(.5)
    


# configure computer selection
    comp = random.randint(1,3)
    # 1 = rock
    # 2 = paper
    # 3 = scissors
    
#retrieve guess from user
    print('Enter your choice:')
    choice = str(input())
   

    #if rock
    if(choice.lower() == 'rock'):

        if(comp == 1):
            print('\nThe computer chose rock!')
            time.sleep(1)
            tie += 1
            print('\nIt\'s a tie! Play again? (yes/no)\n')
            
        elif(comp == 2):
            print('\nThe computer chose paper!')
            time.sleep(1)
            lose += 1
            print('\nYou lose! Play again? (yes/no)\n')
            
        elif(comp == 3):
            print('\nThe computer chose scissors!')
            time.sleep(1)
            win += 1
            print('\nYou win! Play again? (yes/no)\n')
            
    # if paper
    elif(choice.lower() == 'paper'):

        if(comp == 1):
            print('\nThe computer chose rock!')
            time.sleep(1)
            win += 1
            print('\nYou win! Play again? (yes/no)\n')
            
        elif(comp == 2):
            print('\nThe computer chose paper!')
            time.sleep(1)
            tie += 1
            print('\nIt\'s a tie! Play again? (yes/no)\n')
            
        elif(comp == 3):
            print('\nThe computer chose scissors!')
            time.sleep(1)
            lose += 1
            print('\nYou lose! Play again? (yes/no)\n')

    # if scissors
    elif(choice.lower() == 'scissors'):
    
        if(comp == 1):
            print('\nThe computer chose rock!')
            time.sleep(1)
            lose += 1
            print('\nYou lose! Play again? (yes/no)\n')
            
        elif(comp == 2):
            print('\nThe computer chose paper!')
            time.sleep(1)
            win += 1
            print('\nYou win! Play again? (yes/no)\n')
            
        elif(comp == 3):
            print('\nThe computer chose scissors!')
            time.sleep(1)
            tie += 1
            print('\nIt\'s a tie! Play again? (yes/no)\n')
            
    # if user enters other input
    else:
        print('Hmmm... Not quite sure what you said there. Do you want to play again? (yes/no)\n')
        
    play = str(input())

    if play.lower()=='no':
        print('\nThanks for playing!\n')
        print('You won ' + str(win) + ' time(s), lost ' + str(lose) + ' time(s),\
and tied ' + str(tie) + ' time(s).\nBye!')
















      
