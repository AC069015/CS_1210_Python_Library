# Author: Anthony Cunningham

# Exercise 1
def smallestLetters(inputString): # Nested in stringStats
    currentIndex1 = 0
    currentIndex2 = 0
    currentSmallestLetter = inputString[currentIndex1]
    minIndex1 = 0
    currentSmallestLetter2 = inputString[currentIndex2]
    minIndex2 = 0
    for currentLetter in inputString:
        if currentLetter.lower() < currentSmallestLetter.lower():
            currentSmallestLetter = currentLetter
            minIndex1 = currentIndex1
            
        currentIndex1 = currentIndex1 + 1
    print('The smallest letter is ' + currentSmallestLetter.lower() + '.')
    for currentLetter2 in inputString:
        if currentLetter2.lower() <= currentSmallestLetter2.lower():
            if currentLetter2.lower() == currentSmallestLetter.lower():
                currentIndex2 = currentIndex2 + 1
            else:
                currentSmallestLetter2 = currentLetter2
                minIndex2 = currentIndex2
        
        currentIndex2 = currentIndex2 + 1
    print('The second-smallest letter is ' + currentSmallestLetter2.lower() + '.')

def mostCommonLetter(inputString): # Nested in stringStats
    currentIndex = 0
    currentLetter = inputString[currentIndex]
    numberOfA = 0
    numberOfB = 0
    numberOfC = 0
    numberOfD = 0
    numberOfE = 0
    numberOfF = 0
    numberOfG = 0
    numberOfH = 0
    numberOfI = 0
    numberOfJ = 0
    numberOfK = 0
    numberOfL = 0
    numberOfM = 0
    numberOfN = 0
    numberOfO = 0
    numberOfP = 0
    numberOfQ = 0
    numberOfR = 0
    numberOfS = 0
    numberOfT = 0
    numberOfU = 0
    numberOfV = 0
    numberOfW = 0
    numberOfX = 0
    numberOfY = 0
    numberOfZ = 0
    for letter in inputString:
        if currentLetter.lower() == 'a':
            numberOfA = numberOfA + 1
        elif currentLetter.lower() == 'b':
            numberOfB = numberOfB + 1
        elif currentLetter.lower() == 'c':
            numberOfC = numberOfC + 1
        elif currentLetter.lower() == 'd':
            numberOfD = numberOfD + 1
        elif currentLetter.lower() == 'e':
            numberOfE = numberOfE + 1
        elif currentLetter.lower() == 'f':
            numberOfF = numberOfF + 1
        elif currentLetter.lower() == 'g':
            numberOfG = numberOfG + 1
        elif currentLetter.lower() == 'h':
            numberOfH = numberOfH + 1
        elif currentLetter.lower() == 'i':
            numberOfI = numberOfI + 1
        elif currentLetter.lower() == 'j':
            numberOfJ = numberOfJ + 1
        elif currentLetter.lower() == 'k':
            numberOfK = numberOfK + 1
        elif currentLetter.lower() == 'l':
            numberOfL = numberOfL + 1
        elif currentLetter.lower() == 'm':
            numberOfM = numberOfM + 1
        elif currentLetter.lower() == 'n':
            numberOfN = numberOfN + 1
        elif currentLetter.lower() == 'o':
            numberOfO = numberOfO + 1
        elif currentLetter.lower() == 'p':
            numberOfP = numberOfP + 1
        elif currentLetter.lower() == 'q':
            numberOfQ = numberOfQ + 1
        elif currentLetter.lower() == 'r':
            numberOfR = numberOfR + 1
        elif currentLetter.lower() == 's':
            numberOfS = numberOfS + 1
        elif currentLetter.lower() == 't':
            numberOfT = numberOfT + 1
        elif currentLetter.lower() == 'u':
            numberOfU = numberOfU + 1
        elif currentLetter.lower() == 'v':
            numberOfV = numberOfV + 1
        elif currentLetter.lower() == 'w':
            numberOfW = numberOfW + 1
        elif currentLetter.lower() == 'x':
            numberOfX = numberOfX + 1
        elif currentLetter.lower() == 'y':
            numberOfY = numberOfY + 1
        elif currentLetter.lower() == 'z':
            numberOfZ = numberZ + 1
        currentIndex = currentIndex + 1
        currentCommonLetter = currentLetter.lower()
    print('The most common letter is ' + currentCommonLetter + '.')
    
def stringStats(inputString):
    smallestLetters(inputString)
    mostCommonLetter(inputString)

# Exercise 2
def divisorList(number):
    divisor = 1
    listOfDivisors = []
    index = 0
    while divisor <= number:
        if (number % divisor == 0):
            listOfDivisors.append(int(divisor))
        divisor = divisor + 1
    listOfDivisors.sort()
    return(listOfDivisors)

# Exercise 3
def listyMax(listOfLists):
    indexOfList = 0
    indexOfSubList = 0
    currentSubList = listOfLists[indexOfList]
    currentElement = listOfLists[indexOfList][indexOfSubList]
    currentMaxElement = 0
    maxIndex = 0
    subListWithMaxElement = listOfLists[maxIndex]
    for element in listOfLists:
        if len(currentSubList) > 0:
            for element2 in currentSubList:
                if currentElement > currentMaxElement:
                    currentMaxElement = currentElement
                    maxIndex = indexOfSubList
                indexOfSubList = indexOfSubList + 1
        indexOfList = indexOfList + 1
        if len(currentSublist) == 0:
            print('This list is empty.')
    print('In ' + listOfLists + ' the max item is ' + currentMaxElement + ' and is found in sublist ' + subListWithMaxElement + '.')

# Test Functions
def testQ1():
    stringStats('abcdef')
    stringStats('FEDCBA')
    stringStats('AaBbCcDdEeFf')
    stringStats('CaBiNiNtHeWoOdS')

def testQ2():
    print(divisorList(1))
    print(divisorList(11))
    print(divisorList(16))
    print(divisorList(36))
    print(divisorList(121))
    print(divisorList(1001))

def testQ3():
    listyMax([[]])
    listyMax([[1,2], [3,4]])
    listyMax([0,5,10], [l100,99,22],[], [1])
    
    
                
    
