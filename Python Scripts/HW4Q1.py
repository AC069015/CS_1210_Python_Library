# Author: Anthony Cunningham Section A01
# Homeword 4, Question 1

def differByOne(word1, word2): # Nested
    letterDifference = 0
    indexWord2 = 0
    if len(word1) == len(word2):
        for letter1 in word1:
            if word2[indexWord2] != letter1:
                letterDifference = letterDifference + 1
            indexWord2 = indexWord2 + 1
        if letterDifference == 1:
            return True
        else:
            return False
    else:
        return False

def findNeighborWords(word1, wordList): # Nested
    result = []
    for element in wordList:
        word2 = element
        boolean = differByOne(word1, word2)
        differByOne(word1, word2)
        if boolean == True:
            result.append(element)
    
    return [word1, result]

def getWordList(filename): # Nested
    result = []
    fileStream = open(filename, 'r')
    for line in fileStream:
        word = line.strip()
        result.append(word)
    return result

def generateAllNeighborSets(filename): # Nested
    getWordList(filename)
    wordList = filename
    neighborSetsList = []

    for element in wordList:
        findNeighborWords(element, wordList) 
        neighborSetsList.append(findNeighborWords(element, wordList))
    

    return neighborSetsList

def wordNeighborsInfo(filename): # Main Function
    result = generateAllNeighborSets(filename)
    generateAllNeighborSets(filename)
    lonelyWordsList = []

    for element in result:
        if len(element[1]) == 0:
            lonelyWordsList.append(element)
    print("There are " + str(len(lonelyWordsList)) + " 'lonely' words in the file.")

    listOfAllNeighbors = []
    for element in result:
        listOfAllNeighbors.append(element[1])

    lengthOfLOAN = []
    
    for item in listOfAllNeighbors:
        numberOfNeighbors = len(item)
        lengthOfLOAN.append(numberOfNeighbors)
        sumOfNeighbors = sum(lengthOfLOAN)
    avgNeighbors = round((sumOfNeighbors/len(filename)), 2)
    print("The average number of neighbors per word in the file is " + str(avgNeighbors) + '.')
    currentIndex = 0
    maxIndex = 0
    
    while currentIndex <= (len(result) - 1):
        currentElement = result[currentIndex]
        maxElement = result[maxIndex]
        currentNeighborsList = currentElement[1]
        mostNeighbors = maxElement[1]
        if len(currentNeighborsList) > len(mostNeighbors):
            mostNeighbors = currentNeighborsList
            maxIndex = currentIndex
        currentIndex = currentIndex + 1
    print('The word ' + maxElement[0] + ' has the most neighbors, with ' + str(len(mostNeighbors)) + ' neighbors, which are ' + str(mostNeighbors) + '.')
    print()
    print("Next, you can query about the neighbors of any word you like.")
    print("(hit Return/Enter when you want to quit)")
    print()
    query = input("What word do you want to know about? ")
    while query != '':
        if element in filename:
            findNeighborWords(element, filename)
            print(str(element) + ' has ' + str(len(result)) + 'neighbors, which are ' + str(result))
        else:
            print(str(element) + 'is not in query. Please type in another word.')

        query = input("What word do you want to know about? ")

    print("Goodbye!")   
    return

            

