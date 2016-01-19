"""
alpen
EDIT1: changed human(), now excepts other answers and re asks.
EDIT2: gametype added, bof 1, 3, 5
"""
import random
print('LETS PLAY A GAME!\n..........\nROCK!\nPAPER!\nSCISSOR!')
swag = {'paper':1, 'rock':2, 'scissor':3}
def gametype():
    gamepick = (input('Best of 1, 3, or 5? '))
    gtype = {'1', '3', '5'}
    while gamepick not in gtype:
        gamepick = (input('1, 3, or 5. '))
    return gamepick
def inp():
    humanpick = input('WH4T D0 Y0U P!CK $#UP1D HUM4N? ').lower()
    choices = {'paper', 'rock', 'scissor'}
    while humanpick not in choices:
        humanpick = input('REALLY?? PICK AGAIN! ').lower()
    return swag[humanpick]
def pcinp():
    comppick = random.choice(['rock', 'paper', 'scissor'])
    print('RPSMaster5000 picks '+comppick)
    return swag[comppick]
def decide():
    bof = int(gametype())//2
    hpoints = 0
    pcpoints = 0
    while hpoints != bof+1 and pcpoints != bof+1:
        hpick = inp()
        pcpick = pcinp()
        if pcpick < hpick:
            pcpoints += 1
        elif pcpick > hpick:
            hpoints += 1
        else:
            pcpoints += 0
    return hpoints, pcpoints
def whowin():
    human, comp = decide()
    if human > comp:
        print('THAT WAS ALL LUCK!!')
    else:
        print('HAHAHA I NEVER LOSE!!')
whowin()
