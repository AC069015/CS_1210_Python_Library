# Author: Anthony Cunningham Section A01
# Homework 6

# Problem 1

class Box3D():

    def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth

    def setCenter(self, x, y, z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z

    def setWidth(self, newWidth):
        self.width = newWidth

    def setHeight(self, newHeight):
        self.height = newHeight

    def setDepth(self, newDepth):
        self.depth = newDepth

    def volume(self):
        width = self.width
        height = self.height
        depth = self.depth
        volume = (width)*(height)*(depth)
        return volume

    def surfaceArea(self):
        width = self.width
        height = self.height
        depth = self.depth
        surfaceArea = ((2*(width*height)) + (2*(width*depth)) + (2*(height*depth)))
        return(surfaceArea)

    def overlaps(self, otherBox3D):
        if ((self.centerX + (self.width)/2) >= (otherBox3D.centerX - (otherBox3D.width)/2)):
            xOverlap = True
        else:
            return False
        
        if ((self.centerY + ((self.height)/2)) >= (otherBox3D.centerY - ((otherBox3D.height)/2))):
            yOverlap = True
        else:
            return False
        
        if ((self.centerZ + ((self.depth)/2)) >= (otherBox3D.centerZ - ((otherBox3D.depth)/2))):
            zOverlap = True
        else:
            return False

        if xOverlap and yOverlap and zOverlap == True:
            return True

    def __repr__(self):
        return "<{} by {} by {} 3D box centered at point ({}, {}, {})>".format(self.width, self.height, self.depth, self.centerX, self.centerY, self.centerZ)

def testBox3D():
    box1 = Box3D()
    print (box1)
    print(box1.volume())
    print(box1.surfaceArea())
    box1.setCenter(1, 1, 1)
    box1.setWidth(2)
    box1.setHeight(3)
    box1.setDepth(3)
    print(box1)
    print(box1.volume())
    print(box1.surfaceArea())
    box2 = Box3D(4, 4.5, 4.5, 4, 4, 4)
    print(box2) 
    print(box1.overlaps(box2))
    box2.setCenter(4.1, 4.5, 4.5)
    print(box1.overlaps(box2))


# Problem 2

class NimGame():

    def __init__(self, amount):
        self.amount = amount
        print ('Nim game initialized with {} balls.'.format(self.amount))

    def take(self, numberTaken):
        if numberTaken >= 1:
            if numberTaken <= 3:
                newAmount = self.amount - numberTaken
                if newAmount <= 0:
                    print('You took the last of the balls. You lose.')
                else:
                    print('You took {} balls. {} remain.'.format(numberTaken, newAmount))

        else:
            print('Not a valid move; you must select between 1 and 3 balls.')
            
        import random    
        randomNumber = random.randint(1, 3)
        newerAmount = (newAmount) - randomNumber
        if newerAmount <= 0:
            print('The computer took the last of the balls.  You win!')
        else:
            print('Computer took {} balls. {} remain.'.format(randomNumber, newerAmount))

        self.amount = newerAmount


# Problem 3

class Animal (object):
    
    numAnimals = 0

    def __init__ (self, name = 'noname', numLegs = 0):
        self.id = Animal.numAnimals
        Animal.numAnimals = Animal.numAnimals + 1
        self.name = name
        self.numLegs = numLegs

    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("I'm silent")

    def __repr__(self):
        return ('Animal(name={}, numlegs={})'.format(self.name, self.numLegs))
    
    '''def __str__(self):
        return ('<{} the animal(ID#{}))>'.format(self.name, self.id))'''

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching")

    def __repr__(self):
        return 'Dog(name={})'.format(self.name)
    
    def __str__(self):
        return '<{} the dog(ID#{}))>'.format(self.name, self.id)

        
class Cat(Animal):
    
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('Cat(name={}, fur color={})'.format(self.name, self.color))
    
    def __str__(self):
        return ('<{} the {} cat(ID#{}))>'.format(self.name, self.color, self.id))

class Parakeet(Animal):

    def __init__(self, name = 'Perry Saturn'):
        Animal.__init__(self, name, 2)

    def stopMockingMe(self, saySomething):
        print("(in a high-pitched, mimicking shriek) '{}!'".format(saySomething))

    def __repr__(self):
        return('<{} is mocking you!  Are you going to take that from a 3-inch tall bird?>'.format(self.name))

def testParakeetClass():
    iHateThisBird = Parakeet()
    print (iHateThisBird)
    print(iHateThisBird.stopMockingMe('I regret buying this animal.'))
    print(iHateThisBird.stopMockingMe('Do you ever sleep?'))
    print(iHateThisBird.stopMockingMe('Just wait until you meet my barn owl. Just you wait.'))
    

        
                
    
