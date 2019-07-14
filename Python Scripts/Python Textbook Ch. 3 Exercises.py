# Chapter 3
# Exercise 1
def rightJustify(string):
    seventySpaces = (70 - len(string))
    print(('_' * (seventySpaces)) + string)

# Exercise 2
def doTwice(f, v):
    f(v)
    f(v)

def printSpam(v):
    print(v)

def printTwice(string):
    print(string)
    print(string)

def doFour(f, v):
    doTwice(f, v)
    doTwice(f, v)
    



