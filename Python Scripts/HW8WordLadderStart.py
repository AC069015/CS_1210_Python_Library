from HW8BasicGraph import *
from HW8bfs import *

def extractWordLadder(startNode, endNode):
     result = []
     for node in wordGraph:
          currentNode = endNode
          if currentNode == 'none':
               print("There is no word ladder between the two words.  Try a different pair.")
               return
          if currentNode != startNode:
               result.append(currentNode)    
          else:
               return reversed(result)
          currentNode = currentNode.getParent()

def shouldHaveEdge(word1, word2):
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

def buildWordGraph(wordsFile = "words5.text"):
     wordGraph = genCompleteGraph(wordsFile)
     return wordGraph

def findWordLadder(startWord, endWord, wordGraph = buildWordGraph()):
     bfs(wordGraph, startWord)
     wordLadder = extractWordLadder(startWord, endWord)
     return wordLadder

def wordLadder(wordsFile = "words5.text"):
     wordGraph = buildWordGraph()
     query1 = input("Enter a start word. ")
     query2 = input("Enter an end word to see the word ladder connecting the two words. (Press Return to quit) ")
     while query1 or query2 != '':
          inputedWordLadder = findWordLadder(query1, query2)
          
     return inputedWordLadder
