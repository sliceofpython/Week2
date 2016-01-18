#rock, paper, scissors
#chra94

import random

print('Welcome to rock, paper, scissors.')
print("Please choose rock, paper or scissors. Enter '0' for rock, '1' for paper or '2' for scissors.")
select = ['rock', 'paper', 'scissors']
human = select[int(input())]
pc = select[random.randint(0, 2)]
print('You selected ' + str(human) + ', pc selected ' + pc + '.')
if human == pc:
            print("It's a tie!")
elif human == 'rock':
            if pc == 'paper':
                print('PC wins :(')
            else:
                print('You win :)')
elif human == 'paper':
            if pc == 'rock':
                print('You win :)')
            else:
                print('PC wins :(')
else:
    if pc == paper:
            print('You win :)')
    else:
        print('PC wins :(')
