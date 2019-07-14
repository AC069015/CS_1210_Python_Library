# Exercise 1
def printNumbersOnOneLine(ascendingNumber): # nested function
    ascendingNumber2 = 1
    while(ascendingNumber2 <= ascendingNumber):
        print(ascendingNumber2)
        ascendingNumber2 = ascendingNumber2 + 1

def printStuff(low, high): #original function
    ascendingNumber = low
    while(ascendingNumber <= high):
        print(ascendingNumber)
        printNumbersOnOneLine(ascendingNumber)
        ascendingNumber = ascendingNumber + 1


# Exercise 2 ?
def printVowelInformation(inputString):
    vowel1 = 'a'
    vowel2 = 'e'
    vowel3 = 'i'
    vowel4 = 'o'
    vowel5 = 'u'
    numberOfA = 0
    numberOfE = 0
    numberOfI = 0
    numberOfO = 0
    numberOfU = 0
    numberOfConsanants = 0
    currentIndex = 0
    while(currentIndex <= len(inputString)):
        currentLetter = inputString[currentIndex]
        if currentLetter == vowel1:
            (numberOfA + 1)
        elif currentLetter == vowel2:
            (numberOfE + 1)
        elif currentLetter == vowel3:
            (numberOfI + 1)
        elif currentLetter == vowel4:
            (numberOfO + 1)
        elif currentLetter == vowel5:
            (numberOfU + 1)
        else:
            (numberOfConsanants + 1)
        return(numberOfA)
        return(numberOfE)
        return(numberOfI)
        return(numberOfO)
        return(numberOfU)
        return(numberOfConsanants)
        currentIndex = currentIndex + 1
    print("There are " + numberOfA + " a's, " + numberOfE + " e's, " + numberOfI + " i's " + numberOfO + " o's " + numberOfU + " u's " + " and " + numberOfConsanants + " non-vowels in this string.")

# Exercise 3 ?
def maxChar(inputString):
    currentIndex = 0
    currentChar = inputString[currentIndex]
    statementPart1 = 'The max char is '
    statementPart2 = ' and occurs at postition '
    printStatement = print(statementPart1 + currentChar + statementPart2 + currentIndex)
    while(currentIndex <= len(inputString)):
          if (currentChar == 'z'):
              printStatement
          elif (currentChar == 'y'):
              printStatement
          elif (currentChar == 'x'):
              printStatement
          elif (currentChar == 'w'):
              printStatement
          elif (currentChar == 'v'):
              printStatement
          elif (currentChar == 'u'):
              printStatement
          elif (currentChar == 't'):
              printStatement
          elif (currentChar == 's'):
              printStatement
          elif (currentChar == 'r'):
              printStatement
          elif (currentChar == 'q'):
              printStatement
          elif (currentChar == 'p'):
              printStatement
          elif (currentChar == 'o'):
              printStatement
          elif (currentChar == 'n'):
              printStatement
          elif (currentChar == 'm'):
              printStatement
          elif (currentChar == 'l'):
              printStatement
          elif (currentChar == 'k'):
              printStatement
          elif (currentChar == 'j'):
              printStatement
          elif (currentChar == 'i'):
              printStatement
          elif (currentChar == 'h'):
              printStatement
          elif (currentChar == 'g'):
              printStatement
          elif (currentChar == 'f'):
              printStatement
          elif (currentChar == 'e'):
              printStatement
          elif (currentChar == 'd'):
              printStatement
          elif (currentChar == 'c'):
              printStatement
          elif (currentChar == 'b'):
              printStatement
          elif (currentChar == 'a'):
              printStatement      
          currentIndex = currentIndex + 1

# Exercise 4 ?
def binaryRepString(number):
    quotient = number//2
    remainder = number % 2
    while(quotient > 0):
        remainder
        return(remainder)
        quotient
        
    
        
        

        
        

    
    
            
          
            
          
            
