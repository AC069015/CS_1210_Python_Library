# Author: Anthony Cunningham Section A01

# Extra Improvements Made: 1. Made 'Computer's Turn' Button so that the user can manually let the computer take a turn, instead of automatically taking a turn after user took a turn.
#                             Computer's Turn also is a bit more intuitive based on teh situation of the game (ie takes 2 balls when there are three left, etc.)
#
#                          2. Disabled Take 3 and Take 2 buttons when there are less than three or less than two balls left, which is found in the updateGraphic code

from tkinter import Tk, Canvas, Frame, Button, Label, Entry, END, LEFT, RIGHT, SUNKEN
from time import sleep
import random

class NimGame():

    def __init__(self, numberOfBalls):
        self.numberOfBallsRemaining = numberOfBalls
        print("Nim game initialized with {} balls.".format(self.numberOfBallsRemaining))

    def remainingBalls(self):
        return self.numberOfBallsRemaining
    
    def take(self, numberOfBalls):
        if (numberOfBalls < 1) or (numberOfBalls > 3) or (numberOfBalls > self.numberOfBallsRemaining):
            print("You can't take that number of balls. Try again.")
            statusLabel.configure(text="You can't take that number of balls. Try again.")
        else:
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - numberOfBalls
            print("You took {} balls. {} remain.".format(numberOfBalls, self.numberOfBallsRemaining))
            statusLabel.configure(text="You took {} balls. {} remain.".format(numberOfBalls, self.numberOfBallsRemaining))
            if self.numberOfBallsRemaining == 0:
                print("Computer wins!")
                statusLabel.configure(text="Computer wins!")
            else:
                updateGraphics()
                
    def computerTake(self):
        ballsRemaining = self.remainingBalls()
        if ballsRemaining > 3:
            compBallsTaken = random.randint(1,3)
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken
        elif ballsRemaining == 3:
            compBallsTaken = 2
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken
        elif ballsRemaining == 2:
            compBallsTaken = 1
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken
        elif ballsRemaining == 1:
            compBallsTaken = 1
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken

        print("Computer took {} balls. {} remain.".format(compBallsTaken, self.numberOfBallsRemaining))
        statusLabel.configure(text="Computer took {} balls. {} remain.".format(compBallsTaken, self.numberOfBallsRemaining))
        if self.numberOfBallsRemaining == 0:
            print("You win!")
            statusLabel.configure(text="You win!")
        updateGraphics()

canvasHeight = 200
canvasWidth = 610
canvasBorderBuffer = 10
maxBallSize = 100

def updateGraphics():
    ballsRemaining = nimGame.remainingBalls()
    canvas.delete('all')   
    centerX = leftmostBallXPosition
    centerY = ballYPosition
    for i in range(nimGame.remainingBalls()):
        canvas.create_oval(centerX - halfBallSize,
                           centerY - halfBallSize,
                           centerX + halfBallSize,
                           centerY + halfBallSize,
                           fill="#9999ff")
        centerX = centerX + spaceBetweenBalls + ballSize
        canvas.update_idletasks()
    if ballsRemaining < 3:
        button3.configure(state = 'disabled')
        if ballsRemaining < 2:
            button2.configure(state = 'disabled')
    
def takeBalls(numberToTake):
    nimGame.take(numberToTake)

def computerTakeBalls():
    nimGame.computerTake()

def turn():
    nimGame.whosTurn()
    
def initializeNimAndGUI(numberOfBalls):
    global nimGame
    global ballSize, halfBallSize, spaceBetweenBalls, leftmostBallXPosition, ballYPosition

    nimGame = NimGame(numberOfBalls)

    canvas.delete('all') 
    ballSize = min(maxBallSize, int(((canvasWidth-canvasBorderBuffer)//numberOfBalls)/1.2))
    halfBallSize = ballSize // 2
    spaceBetweenBalls = int(0.2 * ballSize)
    leftmostBallXPosition = (canvasBorderBuffer//2) + (spaceBetweenBalls//2) + halfBallSize
    ballYPosition = canvasHeight // 2

    updateGraphics()

def createGUI():
    global rootWindow
    global canvas
    global statusLabel
    global textEntry
    global button2
    global button3
    global button4

    rootWindow = Tk()
    canvasAndButtons = Frame(rootWindow)
    canvas = Canvas(canvasAndButtons, height=canvasHeight, width=canvasWidth, relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)

    buttonframe = Frame(canvasAndButtons)
    button1 = Button(buttonframe, text='Take 1', command=lambda:takeBalls(1))
    button2 = Button(buttonframe, text='Take 2', command=lambda:takeBalls(2))
    button3 = Button(buttonframe, text='Take 3', command=lambda:takeBalls(3))
    button4 = Button(buttonframe, text="Computer's Turn", command=lambda:computerTakeBalls())
    button5 = Button(buttonframe, text='New Game', command=lambda:initializeNimAndGUI(int(entry.get())))
    entry = Entry(buttonframe)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    entry.pack()
    buttonframe.pack(side=RIGHT)
    canvasAndButtons.pack()
    statusLabel = Label(rootWindow, text="Play Nim")
    statusLabel.pack()
    
def runNim(numberOfBalls):
    createGUI()
    initializeNimAndGUI(numberOfBalls)   
    rootWindow.mainloop()




