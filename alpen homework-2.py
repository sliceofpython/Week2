"""
More changes to come, quick game before bed
"""
import random
print('Lets play a game...\n......\n......\nROCK!\nPAPER!\nSCISSOR!')

def comp():
    picks = random.choice(['rock', 'paper', 'scissor'])
    if picks == 'rock':
        print('RPSMaster5000 picked Rock')
    elif picks == 'paper':
        print('RPSMaster5000 picked Paper')
    elif picks == 'scissor':
        print('RPSMaster5000 picked Scissor')
    return picks
def human():
    picks2 = input('Wh4t d0 yOU p1CK $#up!D Hum4N? ')
    return picks2
def counter():
    picks2 = human()
    picks = comp()
    if picks == picks2:
        print('Tie!')
    elif picks == 'rock' and picks2 == 'scissor':
        print('HAHA GET R3KT N00B!')
    elif picks == 'paper' and picks2 == 'rock':
        print('LOL SO EASY!')
    elif picks == 'scissor' and picks2 == 'paper':
        print('I ALWAYS WIN! GIVE UP!')
    else:
        print('LUCKY PICK HUMAN!')
counter()
