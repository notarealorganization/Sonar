# sonar

import random
import sys

def getRow (board, row):

    # return a string for the board data structure at a certain row.
    boardRow = ''
    for i in range (60):
        boardRow += board [i] [row]
    return boardRow



def drawBoard (board):
    # draw the board data structure

    hline = '    ' # initial space for the numbers down the left side of the board
    for i in range (1,6):
        hline += (' ' * 9) + str(i)

    # print numbers across top
    print (hline)
    print ('   ' + ('0123456789' * 6))
    print ()

    # print each of the 15 rows
    for i in range (15):

        # single-digit numbers need to be padded with an extra space
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print ('%s%s %s %s' % (extraSpace, i, getRow(board, i,), i))

    # print the numbers across the bottom
    print ()
    print ('   ' + ('0123456789' * 6))
    print (hline)


def getNewBoard ():
    # create a new 60x15 board data structure
    board = []
    for x in range (60): # the main list is a list of 60 lists
        board.append([])
        for y in range(15) : # each list in the main list has 15 single-charater strings
            # use different charaters for the ocean to make it more readable
            if random.randint(0,1) == 0:
               board[x].append('~')
            else:
               board[x].append('`')
    return board

def getRandomChests (numChests):
    # create a list of chests
    chests = []
    for i in range(numChests):
        chests.append([random.randint (0, 59), random.randint (0, 14)])
    return chests

def isValidMove (x,y):
    # return true if the coorinates are on the board
    return x >= 0 and x <= 59 and y >= 0 and y <= 14


def makeMove (board, chests, x, y):
    # change the board data structure with a sonar device charater.
    # remove treasure chest if they are found
    # return false if invalid, otherwise return the string of the result

    if not isValidMove (x,y):
        return False
    smallestDistance = 100 # any chest will be closer then that

    for cx, cy in chests:
        if abs (cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        if distance < smallestDistance:
            smallestDistance = distance

    if smallestDistance == 0:
        # xy is directly on a treasure chest
        chests.remove([x,y])
        return 'You found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board [x] [y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
        else:
            board [x] [y] = '0'
            return 'Sonar did not detect anything. All treasure chests out of range.'



def enterPlayerMove ():
    # let the player type in her move. return a two-item list of int xy coorinates.
    print('Where do you want to drop the next sonat device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print ('Thanks for playing!')
            sys.exit
        move = move.split ()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print ('Enter a number from 0 to 59, a space, then a number from 0 to 14.')
            


def playAgain ():
    # this funtion returns true if the player want to play again
    print ('Do you want to play again?')
    return input().lower().startswith('y')

def showInstructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to find the three sunken treasure chests that are lurking in the part of the
ocean you are in and collect them.

To play, enter the coordinates of the point in the ocean you wish to drop a
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and the 2's
represent distances of 2 away from the device. The 4's represent
distances of 4 away from the device.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Press enter to continue...''')
    input()

    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the sonar device (the d):

    22222
    c   2
    2 d 2
    2   2
    22222

The point where the device was dropped will be marked with a 2.

The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O

If a device is directly dropped on a treasure chest, you have discovered
the location of the chest, and it will be collected. The sonar device will
remain there.

When you collect a chest, all sonar devices will update to locate the next
closest sunken treasure chest.
Press enter to continue...''')
    input()
    print()



print ('S O N A R')
print ()
print ('Do you want to look at the instructions?')
if input().lower().startswith('y'):
    showInstructions

while True:
    # game setup
    sonarDevices = 16
    theBoard = getNewBoard ()
    theChests = getRandomChests (3)
    drawBoard (theBoard)
    previousMoves = []
    while sonarDevices > 0:
        # start of a turn

        # show sonar device/ chest status
        if sonarDevices > 1: extraSsonar = 's'
        else: extraSsonar = ''

        if len(theChests) > 1: extraSchest = 's'
        else: extraSchest = ''

        print ('You have %s sonar device%s left. %s treasure chest%s remaining' % (sonarDevices, extraSsonar, len(theChests), extraSchest))

        x, y = enterPlayerMove ()
        previousMoves.append([x,y]) # We must track all moves so that sonat devices can be updated

        moveResult = makeMove(theBoard, theChests, x,y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'You found a sunken treasure chest!':
                for x,y in previousMoves:
                   makeMove(theBoard, theChests, x,y)
            drawBoard(theBoard)
            print (moveResult)

        if len(theChests) == 0:
            print ('You found all the treasure chests!')
            break

        sonarDevices -= 1
        if sonarDevices == 0:
            print ('We have run out of sonar devices.')
            print ('We have to go home with the treasure chests still out there')
            print ('    The remain chests were here:')
            for x,y in theChests:
                print ('   %s,%s' % (x,y))
    if not playAgain ():
        sys.exit ()
            
        


        
            

               
            
