# Author: Anthony Cunningham Section A01

# CS Homework 5, Question 1

def reverseLookup(dictName, value):
    for key in dictName:
        if dictName[key] == value:
            print (key, value)

def analyzeSMSes(inputFilename):
    result = []
    fileStream = open(inputFilename, encoding = 'utf-8', 'r')
    for line in fileStream:
        splitLine = line.split()
        cleanSplitLine = splitLine.strip("'/.,?;:+_-)(*&%$#@!{}", "").lower
        result.append(cleanSplitLine)
    return result

    index = 0
    hamDict = {}
    spamDict = {}
    for word in result:
        if result[index][0] == 'ham':
            if word not in hamDict:
                hamDict[word] = 1
            else:
                hamDict[word] += 1
        elif result[index][0] == 'spam':
            if word not in spamDict:
                spamDict[word] = 1
            else:
                spamDict[word] += 1
        index = index + 1
        
    hamValues = hamDict.values()
    spamValues = spamDict.values
    topHamWords = sorted(hamValues, reverse = True)[:10]
    topSpamWords = sorted(spamValues, reverse = True)[:10]

    reverseLookup(hamDict, topHamWords)
    reverseLookup(spamDict, topSpamWords)

    
            

    

    

    

    
